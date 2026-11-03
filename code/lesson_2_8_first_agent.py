"""
Tool-Calling Bakery Agent for Sweet Crumbs.
Can look up bakery prices, check order statuses, answer FAQs from faq.json,
and place new customer orders after asking for explicit human approval in the terminal.
"""

import json
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from pydantic import ValidationError

MAX_STEPS = 5

PRICES: dict[str, int] = {
    "cupcake": 250,
    "brownie": 300,
    "chocolate cake": 1500,
    "red velvet cake": 1800,
}

ORDERS: dict[str, str] = {
    "A101": "Delivered",
    "A102": "out for delivery",
    "A103": "Baking in the oven",
}


@tool(parse_docstring=True)
def get_price(item: str) -> str:
    """Get the price of a Sweet Crumbs bakery item in PKR from the menu.

    Args:
        item: Name of the bakery item (cupcake, brownie, chocolate cake, or red velvet cake).
    """
    key = item.strip().lower()
    if key.endswith("s") and key[:-1] in PRICES:
        key = key[:-1]
    if key in PRICES:
        return f"{key} costs {PRICES[key]} PKR"
    return f"'{item}' is not on our menu. Available items: {', '.join(PRICES.keys())}."


@tool(parse_docstring=True)
def order_status(order_id: str) -> str:
    """Check the current status of an existing customer order by ID.

    Args:
        order_id: The order ID string (for example, A101 or A102).
    """
    oid = order_id.strip().upper()
    if oid in ORDERS:
        return f"Order {oid} is {ORDERS[oid]}"
    return f"Order {oid} was not found."


@tool(parse_docstring=True)
def place_order(item: str, quantity: int, customer: str) -> str:
    """Place a new bakery order after asking the human operator for confirmation.

    Args:
        item: Name of the bakery item to order.
        quantity: Number of items to order (must be at least 1).
        customer: Name of the customer placing the order.
    """
    key = item.strip().lower()
    if key.endswith("s") and key[:-1] in PRICES:
        key = key[:-1]
    if key not in PRICES:
        return f"Cannot place order: '{item}' is not on the menu."
    if quantity <= 0:
        return "Cannot place order: quantity must be at least 1."

    total = PRICES[key] * quantity
    # Why: Never execute state-changing or financial actions without human-in-the-loop approval.
    confirm = input(f"  [approve] {quantity} x {key} for {customer} = {total} PKR. Place it? (yes/no) ").strip().lower()
    if confirm not in ("yes", "y"):
        return f"Order cancelled by operator for {customer}."

    new_id = f"A{101 + len(ORDERS)}"
    ORDERS[new_id] = f"{quantity} x {key} for {customer} (Confirmed)"
    return f"Order {new_id} placed: {quantity} x {key}, total {total} PKR"


@tool(parse_docstring=True)
def read_faq(topic: str) -> str:
    """Look up general bakery FAQ information (hours, location, delivery_policy, custom_cakes).

    Args:
        topic: The FAQ topic or question keyword to look up.
    """
    try:
        with open("faq.json", "r", encoding="utf-8") as f:
            faq = json.load(f)
        return json.dumps(faq, ensure_ascii=False)
    except FileNotFoundError:
        return "FAQ file (faq.json) is not available."


TOOLS = {
    "get_price": get_price,
    "order_status": order_status,
    "place_order": place_order,
    "read_faq": read_faq,
}

# Why: bind_tools passes each tool's JSON schema from its docstring and type hints to the LLM.
llm = ChatOllama(model="llama3.2:3b", temperature=0).bind_tools(list(TOOLS.values()))


def main() -> None:
    messages = [
        SystemMessage(
            content=(
                "You are the Sweet Crumbs Agent. Always use your tools to check prices, "
                "order statuses, FAQs, or place orders. Never guess prices or order statuses."
            )
        )
    ]

    print("Sweet Crumbs Agent: ask about prices, orders, or place an order. Type 'bye' to exit.")

    while True:
        user_text = input("\nYou: ").strip()
        if not user_text:
            continue
        if user_text.lower() == "bye":
            break

        messages.append(HumanMessage(content=user_text))

        # Why: Cap the agent loop with MAX_STEPS so a confused model cannot loop forever calling tools.
        for _ in range(MAX_STEPS):
            ai_msg = llm.invoke(messages)
            messages.append(ai_msg)

            if not ai_msg.tool_calls:
                print(f"Agent: {ai_msg.text}")
                break

            for tool_call in ai_msg.tool_calls:
                t_name = tool_call["name"]
                t_args = tool_call["args"]
                t_id = tool_call["id"]

                if t_name not in TOOLS:
                    result = f"Error: Unknown tool '{t_name}'."
                else:
                    try:
                        result = TOOLS[t_name].invoke(t_args)
                    except (ValidationError, TypeError, ValueError) as err:
                        result = f"Error: Invalid arguments for {t_name}: {err}"

                print(f"  [tool] {t_name}({t_args}) -> {result}")
                messages.append(ToolMessage(content=str(result), tool_call_id=t_id))
        else:
            print("Agent: I reached my maximum thinking steps. Please try rephrasing your request.")


if __name__ == "__main__":
    main()
