"""Task 2.2: Personal Tutor with Memory.

A multi-turn conversational tutor that remembers recent context while capping
memory length so token costs do not grow forever.
"""

from langchain.chat_models import init_chat_model

llm = init_chat_model("qwen2.5:3b", model_provider="ollama", temperature=0.2)

# WHY: Keeping the system prompt at index 0 defines the AI's role and rules
# for the entire session so it never loses its instructions.
messages = [{
    "role": "system",
    "content": (
        "You are a friendly personal tutor. Keep every reply concise "
        "(1 to 2 short sentences)."
    ),
}]

print("Tutor: Ask me anything. Commands: /reset, /count, bye")

while True:
  user_input = input("You: ").strip()

  if not user_input:
    continue

  if user_input.lower() == "bye":
    print("Tutor: Goodbye!")
    break

  if user_input.lower() == "/reset":
    # WHY: Slicing/keeping only messages[0] wipes the conversation history
    # while preserving the core system instructions.
    messages = [messages[0]]
    print("Tutor: Memory cleared.")
    continue

  if user_input.lower() == "/count":
    print(f"Tutor: {len(messages)} messages in memory.")
    continue

  messages.append({"role": "user", "content": user_input})

  # WHY: Trimming to messages[0] + the last 8 messages prevents the prompt
  # from growing indefinitely and keeps input token usage predictable.
  messages = [messages[0]] + messages[1:][-8:]

  response = llm.invoke(messages)
  messages.append({"role": "assistant", "content": response.text})

  input_tokens = response.usage_metadata["input_tokens"]
  print(f"Tutor: {response.text}")
  print(f"       (tokens sent: {input_tokens})")
