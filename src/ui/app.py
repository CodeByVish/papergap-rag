"""Launch from the repository root: python -m streamlit run src/ui/app.py."""

import time
from urllib.parse import urlparse

import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

from src.generation.llm_client import generate
from src.generation.prompting import build_messages, citation_warnings
from src.ui.services import get_retriever, missing_artifacts, rag_config

st.set_page_config(page_title="PaperRAG", page_icon="📄", layout="wide")


def render_result(result, diagnostics):
    st.chat_message("user").write(result["question"])
    if result.get("error"):
        st.error(result["error"])
    if result.get("answer"):
        st.chat_message("assistant").markdown(result["answer"])
        for warning in (citation_warnings(result["answer"], result["passages"]) if result.get("use_rag", True) else []):
            st.warning(warning)
        if result.get("use_rag", True):
            st.caption("Citation labels are checked; support for each claim still needs review.")
        else:
            st.caption("Direct chat · no paper retrieval or evidence citations")
    passages = result.get("passages", [])
    st.caption(
        f"{result['provider']} · {result['model']} · {len(passages)} passages · {result['seconds']:.2f}s"
    )
    if passages:
        with st.expander("Sources and evidence", expanded=True):
            for row in passages:
                st.subheader(
                    f"[{row['evidence_id']}] {row.get('title', row['paper_id'])}"
                )
                section = " › ".join(row.get("section_path", [])) or "Unknown section"
                st.caption(
                    f"{section} · page {row.get('page_start', 'unknown')} · {row['paper_id']}"
                )
                st.text(row["text"])
                url = row.get("source_url", "")
                if urlparse(url).scheme in {"http", "https"} and urlparse(url).netloc:
                    st.link_button("Open source paper", url)
                st.divider()
    if diagnostics:
        with st.expander("Diagnostics"):
            st.json(
                {
                    "provider": result["provider"],
                    "model": result["model"],
                    "seconds": round(result["seconds"], 3),
                    "chunk_ids": [p["chunk_id"] for p in passages],
                    "rrf_scores": [p.get("rrf_score") for p in passages],
                }
            )


def provider_configured(config):
    return isinstance(config, dict) and all(
        isinstance(config.get(k), str)
        and config[k].strip()
        and not config[k].strip().startswith(("replace-", "configure-"))
        for k in ("api_key", "base_url", "model")
    )


def main():
    st.title("📄 PaperRAG")
    st.caption("Ask about NLP papers. Follow every answer back to the evidence.")
    try:
        secrets = st.secrets.to_dict()
    except StreamlitSecretNotFoundError:
        secrets = {}
    except Exception:  # noqa: BLE001 - redact configuration details at the UI boundary
        st.error("Could not read .streamlit/secrets.toml. Check its TOML syntax.")
        return

    with st.sidebar:
        st.header("Settings")
        providers = secrets.get("llm", {})
        choices = ["qwen", "grok", "groq"]
        default = next(
            (i for i, name in enumerate(choices)
             if isinstance(providers, dict) and provider_configured(providers.get(name))),
            0,
        )
        provider = st.selectbox("LLM provider", choices, index=default)
        config = providers.get(provider, {}) if isinstance(providers, dict) else {}
        if not isinstance(config, dict):
            config = {}
        st.caption(f"Model: {config.get('model', 'Not configured')}")
        top_k = st.slider("Evidence passages", 3, 10, 5)
        diagnostics = st.toggle("Show diagnostics", value=False)
        if st.button("Clear answer", use_container_width=True):
            st.session_state.pop("result", None)
        st.caption(
            "Only the latest answer is kept in this browser session. Questions are independent."
        )

    configured = provider_configured(config)
    try:
        cfg = rag_config(secrets.get("rag", {}))
        missing = missing_artifacts(cfg)
    except (TypeError, ValueError):
        st.error("Invalid [rag] configuration. Use the supplied secrets example.")
        return
    mode = st.sidebar.radio(
        "Answer mode", ["Paper RAG", "Direct chat"], index=1 if missing else 0
    )
    use_rag = mode == "Paper RAG"
    if not use_rag:
        st.info("Direct chat: answers use the model's knowledge, without paper retrieval or evidence citations.")
    ready = configured and (not use_rag or not missing)
    if not ready:
        st.info("Finish setup to start asking questions.")
        with st.expander("Setup checklist", expanded=True):
            if not configured:
                st.write(
                    f"Configure the API key, endpoint and model for {provider} in .streamlit/secrets.toml."
                )
            if use_rag and missing:
                st.write("Build the indexes offline. Missing artifacts:")
                st.code("\n".join(missing), language=None)
            st.write("See src/ui/README.md for setup and index-build commands.")
    elif "result" not in st.session_state:
        st.info(
            "Try: What problem does this paper address, and which experiments support its claims?"
        )

    question = st.chat_input(
        "Ask about methods, experiments, findings, or limitations"
    )
    if question and question.strip():
        started = time.perf_counter()
        result = {
            "question": question.strip(),
            "provider": provider,
            "model": config.get("model", "Not configured"),
            "passages": [],
        }
        if not ready:
            result["error"] = (
                f"Configure the API key, endpoint and model for {provider} in .streamlit/secrets.toml."
                if not configured else
                "Paper RAG requires the missing artifacts listed above. Select Direct chat to ask without retrieval."
            )
        elif len(question) > 4000:
            result["error"] = (
                "Please shorten your question to 4,000 characters or fewer."
            )
        else:
            try:
                if use_rag:
                    with st.spinner("Retrieving evidence…"):
                        passages = get_retriever(cfg).retrieve(question.strip(), top_k=top_k)
                else:
                    passages = []
                if use_rag and not passages:
                    result["error"] = "No evidence was retrieved. Try another question or check your indexes."
                else:
                    if use_rag:
                        system, user, evidence = build_messages(question.strip(), passages)
                        result["passages"] = evidence
                    else:
                        system = (
                            "You are a helpful assistant. Paper retrieval is disabled. "
                            "Do not invent evidence citations or claim to have searched the paper corpus."
                        )
                        user = question.strip()
                    result["use_rag"] = use_rag
                    with st.spinner("Generating answer…"):
                        answer = generate(provider, config, system, user)
                    if not answer.strip():
                        result["error"] = (
                            "The provider returned an empty answer. Please try again."
                        )
                    else:
                        result["answer"] = answer
            except Exception as exc:  # noqa: BLE001 - provider errors may contain credentials
                from openai import (
                    APIConnectionError,
                    APITimeoutError,
                    AuthenticationError,
                    RateLimitError,
                )

                if isinstance(exc, AuthenticationError):
                    message = "Provider authentication failed. Check the API key and endpoint."
                elif isinstance(exc, RateLimitError):
                    message = "The provider rate or quota limit was reached. Try later or check your account."
                elif isinstance(exc, (APIConnectionError, APITimeoutError)):
                    message = "Could not reach the provider. Check the endpoint and network, then retry."
                elif isinstance(exc, (ImportError, FileNotFoundError)):
                    message = "Retrieval dependencies or artifacts are missing. Follow src/ui/README.md and check Java."
                else:
                    message = "The request failed. Check the configured model, index metadata and runtime setup, then retry."
                result["error"] = message
        result["seconds"] = time.perf_counter() - started
        st.session_state["result"] = result
    if "result" in st.session_state:
        render_result(st.session_state["result"], diagnostics)


main()
