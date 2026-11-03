"""
WhatsApp Order Extractor for Sweet Crumbs Bakery.
Uses Ollama structured JSON outputs to extract orders from messy English and
Roman Urdu messages, validates items and customer names, and calculates totals in Python.
"""

import json
import ollama

MODEL_NAME = "gemma3:4b"
ORDERS_JSON = "orders.json"
ORDERS_CSV = "orders.csv"

PRICES: dict[str, int] = {
    "cupcake": 250,
    "brownie": 300,
    "chocolate cake": 1500,
    "red velvet cake": 1800,
}

MESSAGES: list[str] = [
    # 1. Normal order
    "Hi! Please send 1 red velvet cake. Sara, House 45 DHA Phase 5.",
    # 2. 2 or more items + Roman Urdu (matches expected output example)
    "Salam! 2 cupcakes aur 1 chocolate cake chahiye. Ali, house 12 Gulberg",
    # 3. Item not on menu (matches expected output example)
    "1 pizza and 2 brownies, Bilal, Model Town",
    # 4. Not an order (matches expected output example)
    "hi do you deliver to Johar Town?",
    # 5. Another Roman Urdu order
    "Mujhe 4 cupcakes aur 2 brownies bhej dein. Zainab, Bahria Town.",
]

ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "is_order": {"type": "boolean"},
        "customer": {"type": "string"},
        "address": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "quantity": {"type": "integer"},
                },
                "required": ["name", "quantity"],
            },
        },
    },
    "required": ["is_order", "customer", "address", "items"],
}

SYSTEM_PROMPT = f"""You extract customer orders from WhatsApp messages for Sweet Crumbs bakery.
Valid menu items are: {', '.join(PRICES.keys())}.
Map plural item names to the exact singular menu item name (e.g., 'cupcakes' -> 'cupcake', 'brownies' -> 'brownie').
If the customer asks for an item NOT on the menu (like 'pizza'), keep its raw lowercase name so Python can flag it.
If the message is just a question and not placing an order, set is_order to false.
Extract the exact customer name and delivery address from the message."""


def extract_message(msg: str) -> dict:
    """Call Ollama with format=ORDER_SCHEMA and temperature 0 to extract structured order data."""
    # Why: Temperature 0 + JSON schema forces deterministic formatting and prevents extra conversational text.
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg},
        ],
        format=ORDER_SCHEMA,
        options={"temperature": 0},
    )
    return json.loads(response["message"]["content"])


def main() -> None:
    valid_orders: list[dict] = []
    total_revenue = 0
    total_checks = 0

    for msg in MESSAGES:
        print(f"Message: {msg}")
        try:
            data = extract_message(msg)
        except json.JSONDecodeError:
            print("  CHECK: AI returned invalid JSON.")
            total_checks += 1
            print()
            continue

        if not data.get("is_order", False):
            print("  Not an order: needs a human reply.\n")
            continue

        customer = data.get("customer", "").strip()
        address = data.get("address", "").strip()
        raw_items = data.get("items", [])

        # Why: Verify the extracted customer name actually appears in the original message to catch AI inventions.
        if not customer or customer.lower() not in msg.lower():
            print(f"  CHECK: Customer name '{customer}' was not found in the message.")
            customer = "Unknown"
            total_checks += 1

        order_lines: list[dict] = []
        order_total = 0
        item_warnings: list[str] = []

        for item_obj in raw_items:
            name = str(item_obj.get("name", "")).strip().lower()
            qty = int(item_obj.get("quantity", 1))

            # Normalize simple plural forms for valid menu items
            if name.endswith("s") and name[:-1] in PRICES:
                name = name[:-1]

            if name in PRICES and qty > 0:
                # Why: Always calculate money in Python—LLMs frequently make arithmetic mistakes.
                line_total = PRICES[name] * qty
                order_total += line_total
                order_lines.append({"item": name, "quantity": qty, "line_total": line_total})
                print(f"  {qty} x {name} = {line_total} PKR")
            else:
                item_warnings.append(f"  CHECK: '{name}' is not on the menu")
                total_checks += 1

        if order_lines:
            print(f"  Customer: {customer}, Address: {address}")
            print(f"  Total: {order_total} PKR")
            valid_orders.append(
                {
                    "customer": customer,
                    "address": address,
                    "items": order_lines,
                    "total": order_total,
                }
            )
            total_revenue += order_total

        for warning in item_warnings:
            print(warning)
        print()

    with open(ORDERS_JSON, "w", encoding="utf-8") as f:
        json.dump(valid_orders, f, indent=2, ensure_ascii=False)

    # Stretch goal: also export line items to orders.csv
    with open(ORDERS_CSV, "w", encoding="utf-8") as f:
        f.write("customer,item,quantity,line_total\n")
        for order in valid_orders:
            for line in order["items"]:
                f.write(f"{order['customer']},{line['item']},{line['quantity']},{line['line_total']}\n")

    print("=" * 50)
    print(f"Orders found: {len(valid_orders)} | Total value: {total_revenue:,} PKR | Checks: {total_checks}")
    print(f"Saved {len(valid_orders)} orders to {ORDERS_JSON}")


if __name__ == "__main__":
    main()
