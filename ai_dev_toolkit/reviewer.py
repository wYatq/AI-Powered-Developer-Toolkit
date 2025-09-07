import os
import openai
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"


def code_review(diff: str) -> str:
    """Call OpenAI to review a git diff."""
    if not openai.api_key:
        return "❌  OPENAI_API_KEY not set."

    prompt = (
        "You are a senior Python engineer. Review the following diff concisely.\n"
        "Focus on performance, security, style. Use emoji bullets.\n\n"
        f"{diff}"
    )
    try:
        rsp = openai.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500,
        )
        return rsp.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️  OpenAI error: {e}"
