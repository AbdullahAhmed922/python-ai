"""
Saved Customer Support Bot for Sweet Crumbs Bakery.
Loads bakery facts from faq.json, persists conversation history across runs,
and catches connection/model errors gracefully while logging them to errors.log.
"""

import json
import sys
from datetime import datetime
import httpx
import ollama

FAQ_FILE = "faq.json"
HISTORY_FILE = "chat_history.json"
ERROR_LOG = "errors.log"
TRANSCRIPT_FILE = "transcript.txt"
MODEL_NAME = "llama3.2:3b"


def log_error(err: Exception) -> None:
    """Append error details with a timestamp to errors.log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {type(err).__name__}: {err}\n")


def load_faq() -> dict:
    """Load business FAQ from faq.json or exit cleanly if missing/damaged."""
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: '{FAQ_FILE}' is missing. Please run from the 'code/' directory.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{FAQ_FILE}' contains invalid JSON. Please check the file syntax.")
        sys.exit(1)


def build_system_prompt(faq: dict) -> str:
    """Build the system message dynamically from the loaded FAQ dictionary."""
    # Why: Building the prompt from faq.json lets the bakery owner update prices without editing Python code.
    price_lines = ", ".join(f"{item}: {price} PKR" for item, price in faq.get("prices", {}).items())
    return (
        f"You are the friendly assistant for {faq.get('business_name')} bakery in {faq.get('location')}. "
        f"Hours: {faq.get('hours')}. "
        f"Delivery: {faq.get('delivery_policy')} "
        f"Custom cakes: {faq.get('custom_cakes')} "
        f"Prices: {price_lines}. "
        "Keep answers concise, polite, and accurate to these facts."
    )


def load_history() -> list[dict[str, str]]:
    """Load previous chat messages, handling missing or corrupted files safely."""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            print("History file format was invalid. Starting a fresh chat.")
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # Why: A corrupted JSON file shouldn't crash the customer's chat session.
        print("History file was damaged. Starting a fresh chat.")
        return []


def save_history(history: list[dict[str, str]]) -> None:
    """Save plain message dictionaries to chat_history.json."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def export_transcript(history: list[dict[str, str]]) -> None:
    """Write the conversation history to a human-readable text file."""
    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        for msg in history:
            f.write(f"{msg['role']}: {msg['content']}\n")
    print(f"Bot: Chat exported to {TRANSCRIPT_FILE}.")


def main() -> None:
    faq = load_faq()
    system_message = {"role": "system", "content": build_system_prompt(faq)}
    history = load_history()

    if history:
        print(f"Loaded {len(history)} old messages.")

    print(f"{faq.get('business_name', 'Sweet Crumbs')} Bot: Ask me anything. Commands: /reset, /export, bye")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if user_input.lower() == "bye":
            save_history(history)
            print("Bot: Goodbye! Your chat is saved.")
            break

        if user_input.lower() == "/reset":
            history.clear()
            save_history(history)
            print("Bot: Chat history cleared.")
            continue

        if user_input.lower() == "/export":
            export_transcript(history)
            continue

        history.append({"role": "user", "content": user_input})

        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=[system_message] + history,
            )
            reply_text = response["message"]["content"].strip()
            print(f"Bot: {reply_text}")
            history.append({"role": "assistant", "content": reply_text})
            save_history(history)

        except httpx.ConnectError as err:
            # Why: Remove the unanswered user message so failed turns don't pollute future context.
            history.pop()
            log_error(err)
            print("Bot: I am offline right now. Please open the Ollama app and try again.")

        except ollama.ResponseError as err:
            history.pop()
            log_error(err)
            print("Bot: My AI model had a hiccup. Please check that the model is pulled and try again.")


if __name__ == "__main__":
    main()
