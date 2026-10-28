"""Task 2.3: Sweet Crumbs Bakery Persona Bot that grounds answers strictly in
real business facts, switches personas safely, and looks up prices directly."""

from langchain.chat_models import init_chat_model

# Why: Centralizing model settings in a config dictionary makes it easy to tune
# model name, creativity, and memory window in one place instead of hunting through code.
config = {
    "model": "ollama:qwen2.5:3b",
    "temperature": 0.2,
    "memory_size": 8,
}

facts = {
    "name": "Sweet Crumbs",
    "type": "Artisan Bakery",
    "city": "Lahore",
    "hours": "8:00 AM to 10:00 PM daily",
    "delivery": "Free delivery in Lahore on orders above 2000 PKR",
    "prices": {
        "chocolate cake": 1500,
        "cupcake": 250,
        "brownie": 300,
        "cookie": 150,
    },
}

personas = {
    "friendly": "warm and cheerful, uses simple words",
    "formal": "polite, professional, and concise",
    "sales": "excited, always suggests one extra item to buy",
}


def build_system_message(business_facts: dict, style: str) -> str:
    """Build the system prompt from the facts dictionary and selected persona style."""
    price_lines = ", ".join(
        f"{item.title()}: {price} PKR"
        for item, price in business_facts["prices"].items()
    )
    # Why: Injecting the exact facts and instructing the AI to ONLY use them
    # prevents hallucinated menu items or made-up prices.
    return (
        f"You are the assistant for {business_facts['name']}, an {business_facts['type']} "
        f"in {business_facts['city']}.\n"
        f"Opening hours: {business_facts['hours']}.\n"
        f"Delivery policy: {business_facts['delivery']}.\n"
        f"Menu and prices ( baked fresh every morning ): {price_lines}.\n"
        f"Speaking style: {style}.\n"
        "IMPORTANT: Only use these facts. If a customer asks for an item or fact not listed "
        "above, politely admit that you do not have or know it. Keep replies to 1-2 sentences."
    )


llm = init_chat_model(config["model"], temperature=config["temperature"])

messages = [
    {"role": "system", "content": build_system_message(facts, personas["friendly"])}
]

print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, bye")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    if user_input.lower().startswith("/persona"):
        parts = user_input.split(maxsplit=1)
        chosen_name = parts[1].lower() if len(parts) > 1 else ""
        # Why: Using .get() with a fallback default ensures an unknown persona name
        # never raises a KeyError crash.
        style = personas.get(chosen_name, personas["friendly"])
        messages[0]["content"] = build_system_message(facts, style)
        print(f"Bot: Style changed to: {style}")
        continue

    if user_input.lower().startswith("/price"):
        raw_item = user_input[6:].strip()
        lookup_key = raw_item.lower()
        # Why: Direct dictionary lookup for prices is instant, costs 0 tokens,
        # and guarantees 100% accuracy without calling the LLM.
        if lookup_key in facts["prices"]:
            print(f"Bot: {raw_item} costs {facts['prices'][lookup_key]} PKR.")
        else:
            print(f"Bot: Sorry, {raw_item} is not on our menu.")
        continue

    messages.append({"role": "user", "content": user_input})

    response = llm.invoke(messages)
    messages.append({"role": "assistant", "content": response.text})

    messages = [messages[0]] + messages[1:][-config["memory_size"] :]

    print(f"Bot: {response.text.strip()}")
