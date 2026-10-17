from openai import OpenAI


def generate(provider, config, system_prompt, user_prompt):
    client = OpenAI(
        api_key=config["api_key"],
        base_url=config["base_url"],
        timeout=90.0,
        max_retries=2,
    )
    model = config["model"]

    if provider == "qwen":
        result = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
        )
        return result.choices[0].message.content or ""

    if provider == "grok":
        result = client.responses.create(
            model=model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return result.output_text or ""

    raise ValueError(f"Unknown provider: {provider}")
