"""Task 2.4: Batch Product Writer for Sweet Crumbs bakery that generates
one-sentence menu descriptions and tracks total token and time cost."""

from langchain.chat_models import init_chat_model

products = {
    "Old Stock": 0,
    "Chocolate Cake": 1500,
    "Cupcake": 250,
    "Brownie": 300,
    "Donut": 200,
}

# Why: Creating the model once outside the loop avoids re-initializing the client
# on every iteration, keeping the batch run fast and clean.
llm = init_chat_model("ollama:qwen2.5:3b", temperature=0.3)

results = []
# Why: Accumulators must start at 0 before the loop so each iteration can add
# its token count and duration to a running total.
total_tokens = 0
total_seconds = 0.0

for name, price in products.items():
    # Why: Skipping items with price 0 via continue avoids wasting an AI call
    # and spending tokens on unavailable products.
    if price == 0:
        print(f"Skipping {name.lower()} (no price)")
        continue

    prompt = [
        {
            "role": "system",
            "content": (
                "You are a copywriter for Sweet Crumbs bakery in Lahore. "
                "Write exactly one short, mouth-watering menu sentence for the given item. "
                "Do not include the price or item title in your sentence."
            ),
        },
        {"role": "user", "content": f"Item: {name} ({price} PKR)"},
    ]

    response = llm.invoke(prompt)

    results.append(
        {
            "item": name,
            "price": price,
            "text": response.text.strip(),
        }
    )

    total_tokens += response.usage_metadata["total_tokens"]
    total_seconds += response.response_metadata["total_duration"] / 1_000_000_000

print("=" * 50)
for idx, entry in enumerate(results, start=1):
    print(f"{idx}. {entry['item']} ({entry['price']} PKR)")
    print(f"   {entry['text']}")
print("=" * 50)
print(
    f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds"
)
