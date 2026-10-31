"""LangGraph agent for PaperGap adaptive retrieval (P4).

    plan_question -> retrieve -> map_evidence -> critic
        -> [sufficient, retry budget spent or INSUFFICIENT_INFORMATION] -> END
        -> [otherwise] -> rewrite_query -> retrieve (loop)

The critic assigns the gap label itself, so there is no separate classifier node.
"""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from src.agent.critic import DEFAULT_ATTEMPTS, CriticClient, make_critic_node
from src.agent.nodes import (
    DEFAULT_TOP_K,
    MAX_RETRIES,
    Retriever,
    SectionSelector,
    make_retrieve_node,
    map_evidence,
    plan_question,
    route_after_critic,
)
from src.agent.rewriter import rewrite_query
from src.agent.schemas import AgentState


def build_agent_graph(
    retriever: Retriever,
    max_retries: int = MAX_RETRIES,
    top_k: int = DEFAULT_TOP_K,
    critic_client: CriticClient | None = None,
    critic_attempts: int = DEFAULT_ATTEMPTS,
    section_selector: SectionSelector | None = None,
) -> CompiledStateGraph:
    """Compile the agent around `retriever(query, paper_id, top_k)`.

    With `critic_client` the critic asks the LLM and falls back to rules on a bad
    reply; without one it uses the rule-based check only.

    `max_retries` counts retries after the initial retrieval, so at most
    `max_retries + 1` retrieval rounds run.
    """
    if max_retries < 0:
        raise ValueError("max_retries must be non-negative")
    max_rounds = max_retries + 1

    def route(state: AgentState):
        return route_after_critic(state, max_rounds)

    graph = StateGraph(AgentState)
    graph.add_node("plan_question", plan_question)
    graph.add_node("retrieve", make_retrieve_node(retriever, top_k, section_selector))
    graph.add_node("map_evidence", map_evidence)
    graph.add_node("critic", make_critic_node(critic_client, critic_attempts))
    graph.add_node("rewrite_query", rewrite_query)

    graph.add_edge(START, "plan_question")
    graph.add_edge("plan_question", "retrieve")
    graph.add_edge("retrieve", "map_evidence")
    graph.add_edge("map_evidence", "critic")
    graph.add_conditional_edges(
        "critic", route, {"retry": "rewrite_query", "stop": END}
    )
    graph.add_edge("rewrite_query", "retrieve")

    return graph.compile()
