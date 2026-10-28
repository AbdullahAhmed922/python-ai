"""Task 2.1: AI Tutor.

Explains any user-chosen topic at a beginner or expert level using a local
Ollama model and reports token usage and execution time.
"""

from langchain.chat_models import init_chat_model

# WHY: .strip() removes accidental leading/trailing spaces from user terminal input
# so the prompt stays clean and consistent.
topic = input("Topic: ").strip()
level = input("Level (beginner or expert): ").strip()

# WHY: A low temperature (0.2) keeps the tutor's explanations factual, focused,
# and consistent across runs rather than overly random.
llm = init_chat_model("qwen2.5:3b", model_provider="ollama", temperature=0.2)

messages = [
    {
        "role": "system",
        "content": (
            f"You are a clear, supportive tutor teaching a {level} student. "
            "Explain the topic in strictly 3 short sentences."
        ),
    },
    {
        "role": "user",
        "content": f"Explain {topic}.",
    },
]

response = llm.invoke(messages)

print("=" * 40)
print(response.text)
print("=" * 40)

total_tokens = response.usage_metadata["total_tokens"]
# WHY: Ollama reports total_duration in nanoseconds, so dividing by 1e9 converts it to seconds.
seconds = response.response_metadata["total_duration"] / 1e9

print(f"{total_tokens} tokens in {seconds:.1f} seconds")
