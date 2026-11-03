"""
AI Skills Toolkit for Sweet Crumbs Bakery.
Provides reusable AI-powered functions for daily bakery operations:
summarizing customer inquiries, translating order updates, and replying to reviews.
"""

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# Why: Create models once at the top to avoid re-initializing connections on every function call.
precise_model = ChatOllama(model="gemma3:4b", temperature=0.1)
creative_model = ChatOllama(model="gemma3:4b", temperature=0.8)


def ask_ai(
    prompt: str,
    system: str = "You are a helpful assistant for Sweet Crumbs bakery in Lahore.",
    creative_mode: bool = False,
) -> str:
    """Send a prompt to the appropriate local Ollama model and return the text response."""
    # Why: Pick temperature based on whether the task needs factual accuracy or creative warmth.
    model = creative_model if creative_mode else precise_model
    messages = [SystemMessage(content=system), HumanMessage(content=prompt)]
    response = model.invoke(messages)
    return response.text.strip()


def estimate_tokens(text: str) -> int:
    """Roughly estimate token count without calling the AI (approx. 4 characters per token)."""
    if not text:
        return 0
    return max(1, len(text) // 4)


# Why: Verify helper logic immediately on startup so broken math never reaches production.
assert estimate_tokens("") == 0
assert estimate_tokens("Cake") == 1
assert estimate_tokens("Cake was great but delivery was late.") == 9


def summarize(text: str) -> str:
    """Summarize a long customer message or custom cake request into one clear sentence."""
    prompt = f"Summarize this customer message in one short sentence:\n\n{text}"
    return ask_ai(prompt, creative_mode=False)


def translate(text: str, language: str = "Urdu") -> str:
    """Translate an order notification or message into the target language (defaults to Urdu)."""
    prompt = f"Translate the following text into {language}. Output ONLY the translation:\n\n{text}"
    return ask_ai(prompt, creative_mode=False)


def reply_to_review(review: str) -> str:
    """Write a warm, polite 2-sentence reply to a customer review for Sweet Crumbs bakery."""
    prompt = f"Write a warm 2-sentence reply from Sweet Crumbs bakery to this customer review:\n\n{review}"
    return ask_ai(prompt, creative_mode=True)


def main() -> None:
    usage: dict[str, int] = {
        "summarize": 0,
        "translate": 0,
        "reply": 0,
        "batch": 0,
    }

    print("Sweet Crumbs AI Toolkit. Commands: /summarize, /translate, /reply, /batch, bye")

    while True:
        cmd = input("\nCommand: ").strip().lower()

        if cmd == "bye":
            break
        elif cmd == "/summarize":
            text = input("Text to summarize: ").strip()
            print(f"AI: {summarize(text)}")
            usage["summarize"] += 1
        elif cmd == "/translate":
            text = input("Text to translate: ").strip()
            lang = input("Language (Enter for Urdu): ").strip()
            result = translate(text) if not lang else translate(text, lang)
            print(f"AI: {result}")
            usage["translate"] += 1
        elif cmd == "/reply":
            review = input("Customer review: ").strip()
            tokens = estimate_tokens(review)
            print(f"AI: {reply_to_review(review)}")
            print(f"    (review was about {tokens} tokens)")
            usage["reply"] += 1
        elif cmd == "/batch":
            sample_reviews = [
                "Cake was great but delivery was late.",
                "Best fudge brownies in Lahore, super fresh!",
                "Cupcakes looked lovely for our party, thank you!",
            ]
            for idx, rev in enumerate(sample_reviews, start=1):
                print(f"[{idx}] Review: {rev}")
                print(f"    Reply: {reply_to_review(rev)}")
            usage["batch"] += 1
        else:
            print("Unknown command. Try /summarize, /translate, /reply, /batch or bye.")

    print("\nSkills used today:")
    for skill, count in usage.items():
        print(f"  {skill}: {count}")


if __name__ == "__main__":
    main()
