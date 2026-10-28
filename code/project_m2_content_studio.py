"""
AI Content Studio for Sweet Crumbs bakery in Lahore.
Writes batch menu descriptions, streams toned social media posts (with Roman Urdu
translations), answers prices directly from dictionary data without calling the AI,
and chats with customers using grounded facts and sliding-window memory.
"""

from langchain.chat_models import init_chat_model

# --- A. Setup and Data ---

config = {
    "model": "ollama:gemma3:4b",  # Or "ollama:llama3.2:3b"
    "max_messages": 6,
    "cloud_cost_per_1k_tokens": 0.015,  # Bonus: example cloud price in USD per 1K tokens
}

facts = {
    "name": "Sweet Crumbs",
    "city": "Lahore",
    "hours": "9 am to 10 pm",
    "delivery": "200 PKR across Lahore (including DHA), and free for orders from 3,000 PKR",
    "custom_orders": "24 hours advance notice for custom cakes",
    "prices": {
        "chocolate cake": 1500,
        "cupcake": 250,
        "brownie": 300,
        "mango tart": 0,
    },
}

tones = {
    "fun": "playful and full of energy, short sentences",
    "premium": "elegant and calm, focused on quality",
    "urgent": "fresh-out-of-the-oven limited batch alert, encouraging quick orders today",
}

# WHY: We create both models once at the top so we do not re-initialize them on every user turn.
# Low temperature (0.2) keeps customer answers factual; high temperature (0.8) makes marketing copy creative.
precise_llm = init_chat_model(config["model"], temperature=0.2)
creative_llm = init_chat_model(config["model"], temperature=0.8)

price_summary = ""
for item_name, item_price in facts["prices"].items():
    if item_price == 0:
        price_summary += f"- {item_name.title()}: Coming soon\n"
    else:
        price_summary += f"- {item_name.title()}: {item_price:,} PKR\n"

# WHY: Putting all business facts into the system message grounds the AI so it never invents prices or items.
system_prompt = f"""You are the helpful customer assistant for {facts["name"]} bakery in {facts["city"]}.
You must ONLY use the bakery facts below to answer questions.
If a customer asks about anything not covered in these facts, say sorry and state that you only know about {facts["name"]} bakery items. Keep answers short (1 to 2 sentences).

Bakery Facts:
- Name: {facts["name"]}
- City: {facts["city"]}
- Hours: {facts["hours"]}
- Delivery: {facts["delivery"]}
- Custom Orders: {facts["custom_orders"]}
- Menu & Prices:
{price_summary}"""

messages = [{"role": "system", "content": system_prompt}]

# Session accumulators
chat_count = 0
menu_count = 0
post_count = 0
price_count = 0
total_tokens = 0
total_seconds = 0.0

# --- B. The Command Loop ---

print("=" * 50)
print(f"   {facts['name']} AI Content Studio")
print("=" * 50)
print("Commands: /menu, /post fun|premium|urgent, /price <item>, /reset, bye")

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    command_lower = user_input.lower()

    if command_lower == "bye":
        print("Studio: Goodbye!")
        break

    # --- C. /menu: Batch Descriptions ---
    elif command_lower == "/menu":
        menu_list = []
        menu_tokens = 0

        for item_name, item_price in facts["prices"].items():
            # WHY: Skip price-0 items before calling the AI so we spend zero tokens on unavailable items.
            if item_price == 0:
                print(f"Studio: Skipping {item_name} (coming soon)")
                continue

            prompt = (
                f"Write a one-sentence delicious bakery description for '{item_name.title()}' "
                f"at {facts['name']} in {facts['city']}. Return only the single sentence."
            )
            response = creative_llm.invoke(prompt)

            call_tokens = response.usage_metadata.get("total_tokens", 0)
            call_seconds = response.response_metadata.get("total_duration", 0) / 1_000_000_000

            total_tokens += call_tokens
            menu_tokens += call_tokens
            total_seconds += call_seconds
            menu_count += 1

            menu_list.append({
                "name": item_name.title(),
                "price": item_price,
                "description": response.text.strip(),
            })

        print("-" * 50)
        for index, entry in enumerate(menu_list, start=1):
            print(f"{index}. {entry['name']} ({entry['price']:,} PKR)")
            print(f"   {entry['description']}")
        print("-" * 50)

        # Bonus (+5): Cloud cost estimate for the menu batch
        cloud_cost = (menu_tokens / 1000) * config["cloud_cost_per_1k_tokens"]
        print(
            f"Studio: Menu batch used {menu_tokens:,} tokens "
            f"(estimated cloud cost: ${cloud_cost:.2f})"
        )

    # --- D. /post <tone>: Streamed Social Media Post ---
    elif command_lower.startswith("/post"):
        tone_key = command_lower[5:].strip()
        # WHY: .get() with a default ensures an invalid tone like '/post pirate' falls back safely without a KeyError.
        tone_description = tones.get(tone_key, tones["fun"])

        print(f"Studio ({tone_description}):")

        post_prompt = (
            f"Write a short 3-line Instagram post for {facts['name']} bakery in {facts['city']}. "
            f"Style: {tone_description}. "
            f"Mention one available item and its exact PKR price from:\n{price_summary}"
            f"End with our city ({facts['city']}) and hours (Open {facts['hours']})."
        )

        english_post = ""
        for chunk in creative_llm.stream(post_prompt):
            print(chunk.text, end="", flush=True)
            english_post += chunk.text
            if chunk.usage_metadata:
                total_tokens += chunk.usage_metadata.get("total_tokens", 0)
            if chunk.response_metadata and "total_duration" in chunk.response_metadata:
                total_seconds += chunk.response_metadata.get("total_duration", 0) / 1_000_000_000
        print()
        post_count += 1

        # Bonus (+5): Roman Urdu version using the precise model and English post as input
        urdu_prompt = (
            f"Translate this bakery Instagram post into natural Pakistani Roman Urdu. "
            f"Keep the exact PKR price and opening hours unchanged. Return only the Roman Urdu lines:\n\n{english_post}"
        )
        urdu_response = precise_llm.invoke(urdu_prompt)
        total_tokens += urdu_response.usage_metadata.get("total_tokens", 0)
        total_seconds += urdu_response.response_metadata.get("total_duration", 0) / 1_000_000_000
        print("\nStudio (Roman Urdu):")
        print(urdu_response.text.strip())

    # --- E. /price <item>: Instant Dictionary Lookup (No AI) ---
    elif command_lower.startswith("/price"):
        item_lookup = command_lower[6:].strip()
        price_count += 1

        # WHY: Dictionary lookup is deterministic, instant, and costs 0 AI tokens.
        found_price = facts["prices"].get(item_lookup)

        if found_price is None:
            print(f"Studio: {item_lookup.title()} is not on our menu.")
        elif found_price == 0:
            print(f"Studio: {item_lookup.title()} is coming soon.")
        else:
            print(f"Studio: {item_lookup.title()} costs {found_price:,} PKR.")

    # --- /reset: Clear Chat Memory ---
    elif command_lower == "/reset":
        messages = [messages[0]]
        print("Studio: Conversation memory cleared.")

    # --- E. Customer Chat with Memory ---
    else:
        messages.append({"role": "user", "content": user_input})

        # WHY: Keep messages[0] (system rules) plus the last max_messages so memory stays bounded.
        if len(messages) > config["max_messages"] + 1:
            messages = [messages[0]] + messages[-config["max_messages"]:]

        response = precise_llm.invoke(messages)
        messages.append({"role": "assistant", "content": response.text})

        sent_tokens = response.usage_metadata.get("input_tokens", 0)
        call_tokens = response.usage_metadata.get("total_tokens", 0)
        call_seconds = response.response_metadata.get("total_duration", 0) / 1_000_000_000

        total_tokens += call_tokens
        total_seconds += call_seconds
        chat_count += 1

        print(f"Studio: {response.text.strip()}")
        print(f"        (memory: {len(messages)} messages, {sent_tokens} tokens sent)")

# --- F. Session Report ---
print("=" * 50)
print("Session report")
print(
    f"Chat answers: {chat_count} | Menu descriptions: {menu_count} | "
    f"Posts: {post_count} | Price answers: {price_count}"
)
print(f"AI usage: {total_tokens:,} tokens in {total_seconds:.1f} seconds")
print("=" * 50)
