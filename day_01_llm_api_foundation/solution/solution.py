"""
Day 1 — LLM API Foundation
AICB-P1: AI Practical Competency Program, Phase 1

Instructions:
    1. Fill in every section marked with TODO.
    2. Do NOT change function signatures.
    3. Copy this file to solution/solution.py when done.
    4. Run: pytest tests/ -v
"""

import os
import time
from typing import Any, Callable
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# ---------------------------------------------------------------------------
# Estimated costs per 1K OUTPUT tokens (USD)
# ---------------------------------------------------------------------------
COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

OPENAI_MODEL = "gpt-4o"
OPENAI_MINI_MODEL = "gpt-4o-mini"


# ---------------------------------------------------------------------------
# Task 1 — Call GPT-4o
# ---------------------------------------------------------------------------
def call_openai(
    prompt: str = "What is the capital of France?",
    model: str = OPENAI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    """
    Call the OpenAI Chat Completions API and return the response text + latency.
    """
    # TODO: Initialize OpenAI client
    # TODO: Record start time
    # TODO: Call client.chat.completions.create with the given parameters
    # TODO: Calculate latency
    # TODO: Extract response text from response.choices[0].message.content
    # TODO: Return (response_text, latency)
    pass


# ---------------------------------------------------------------------------
# Task 2 — Call GPT-4o-mini
# ---------------------------------------------------------------------------
def call_openai_mini(
    prompt: str = "What is the capital of France?",
    model: str = OPENAI_MINI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    """
    Call the OpenAI Chat Completions API using gpt-4o-mini.
    """
    # TODO: Reuse call_openai with the mini model
    pass


# ---------------------------------------------------------------------------
# Task 3 — Compare GPT-4o vs GPT-4o-mini
# ---------------------------------------------------------------------------
def compare_models(prompt: str) -> dict:
    """
    Call both models and return a comparison dict with responses, latencies, and cost estimate.
    """
    # TODO: Call call_openai (model=OPENAI_MODEL) and call_openai_mini
    # TODO: Estimate cost based on output token count
    # TODO: Return dict with keys:
    #   gpt4o_response, mini_response, gpt4o_latency, mini_latency, gpt4o_cost_estimate
    pass


# ---------------------------------------------------------------------------
# Task 4 — Streaming chatbot with conversation history
# ---------------------------------------------------------------------------
def streaming_chatbot() -> None:
    """
    Interactive streaming chatbot with 3-turn history.
    """
    # TODO: Initialize OpenAI client and empty messages list
    # TODO: Loop: get user input, exit on 'quit'/'exit'
    # TODO: Append user message to history
    # TODO: Trim history to last 6 messages (3 turns)
    # TODO: Call API with stream=True, print chunks as they arrive
    # TODO: Append assistant response to history
    pass


# ---------------------------------------------------------------------------
# Bonus Task A — Retry with exponential backoff
# ---------------------------------------------------------------------------
def retry_with_backoff(
    fn: Callable,
    max_retries: int = 3,
    base_delay: float = 0.1,
) -> Any:
    """
    Call fn(), retrying up to max_retries times with exponential backoff on failure.
    """
    # TODO: Loop up to max_retries + 1 times
    # TODO: On success, return result
    # TODO: On exception, wait base_delay * (2 ** attempt) seconds, then retry
    # TODO: After max_retries exhausted, raise the last exception
    pass


# ---------------------------------------------------------------------------
# Bonus Task B — Batch compare
# ---------------------------------------------------------------------------
def batch_compare(prompts: list[str]) -> list[dict]:
    """
    Run compare_models on a list of prompts and return results with prompt included.
    """
    # TODO: For each prompt, call compare_models and add 'prompt' key to result
    pass


# ---------------------------------------------------------------------------
# Bonus Task C — Format comparison table
# ---------------------------------------------------------------------------
def format_comparison_table(results: list[dict]) -> str:
    """
    Format batch_compare results as a readable text table.
    """
    # TODO: Build a header row with columns: Prompt, GPT-4o, Mini, Lat 4o, Lat Mini
    # TODO: For each result, truncate long strings and format as a row
    # TODO: Return the full table as a string
    pass


if __name__ == "__main__":
    # Quick smoke test — replace with your own prompt
    test_prompt = "Why is the sky blue?"
    print("=== Model Comparison ===")
    print(compare_models(test_prompt))

    print("\n=== Streaming Chatbot (type 'quit' to exit) ===")
    streaming_chatbot()
