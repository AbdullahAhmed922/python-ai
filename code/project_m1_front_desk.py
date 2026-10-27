"""
Sweet Crumbs Bakery — AI Front Desk Assistant
Answers common bakery FAQs using rules, calculates exact order quotes with bulk
discounts and delivery fees, routes unanswered questions to local or cloud AI
models with token/cost estimates, and prints a session summary report.
"""

# Constants in UPPER_CASE so prices and thresholds can be updated in one place
BOT_NAME = "Sweet Crumbs Desk"
BUSINESS_NAME = "Sweet Crumbs bakery"

CUPCAKE_PRICE = 250
BROWNIE_PRICE = 300
CHOCOLATE_CAKE_PRICE = 1500

BULK_MIN_QTY = 10
BULK_DISCOUNT_RATE = 0.10

DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000

CLOUD_PRICE_PER_1K_TOKENS = 0.10

# Session counters
total_messages = 0
answered_by_rules = 0
unanswered_questions = 0
total_quotes = 0
total_quoted_value = 0
total_ai_cost = 0.0
complaint_count = 0

print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.\n")

# Ask the customer's name once before the loop and clean formatting
customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()
if customer_name == "":
    customer_name = "Guest"

while True:
    raw_input = input(f"\n{customer_name}: ")
    message = raw_input.strip().lower()

    # Ignore empty inputs so accidental Enter presses do not trigger the AI fallback
    if message == "":
        print(f"{BOT_NAME}: Please type a message, /quote, or bye.")
        continue

    total_messages += 1

    # Exit condition
    if message == "bye":
        answered_by_rules += 1
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    # Bonus (+5): Human handover keyword ends the chat immediately
    if "human" in message or "agent" in message:
        answered_by_rules += 1
        print(f"{BOT_NAME}: Connecting you to a human...")
        break

    # WHY: Complaint rule comes FIRST so an upset customer asking about hours/prices
    # still gets prioritized for human manager escalation instead of a generic FAQ reply.
    if "refund" in message or "complaint" in message or "late" in message:
        answered_by_rules += 1
        complaint_count += 1
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")

    # C. /quote price calculator
    elif message == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        qty_text = input(f"{BOT_NAME}: How many? ").strip()

        # Bonus (+5): Check .isdigit() before int() so typing letters does not crash with ValueError
        if not qty_text.isdigit():
            print(f"{BOT_NAME}: Please enter a whole number for the quantity (e.g. 6).")
            continue

        quantity = int(qty_text)
        if quantity <= 0:
            print(f"{BOT_NAME}: Quantity must be at least 1.")
            continue

        # Match item price with if / elif / else
        if item == "cupcake":
            unit_price = CUPCAKE_PRICE
        elif item == "brownie":
            unit_price = BROWNIE_PRICE
        elif item == "chocolate cake":
            unit_price = CHOCOLATE_CAKE_PRICE
        else:
            unit_price = 0

        if unit_price == 0:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
        else:
            subtotal = unit_price * quantity

            # Bulk discount rule: 10% off for 10 or more items
            if quantity >= BULK_MIN_QTY:
                discount = int(subtotal * BULK_DISCOUNT_RATE)
            else:
                discount = 0

            discounted_subtotal = subtotal - discount

            # WHY: Check free-delivery eligibility AFTER applying the discount so the bakery
            # does not give free delivery on orders that drop below 3,000 PKR after discount.
            if discounted_subtotal >= FREE_DELIVERY_LIMIT:
                delivery = 0
            else:
                delivery = DELIVERY_FEE

            order_total = discounted_subtotal + delivery

            total_quotes += 1
            total_quoted_value += order_total

            print(f"{BOT_NAME}: {quantity} x {item} = {subtotal:,} PKR")
            print(f"     Discount: -{discount:,} PKR | Delivery: {delivery:,} PKR")
            print(f"     Total: {order_total:,} PKR")

    # WHY: Check greetings with == or .startswith() (with a trailing space) instead of 'in'
    # because 'hi' is inside words like 'which', 'this', and 'white'.
    elif (
        message == "hi"
        or message == "hello"
        or message == "salam"
        or message == "hey"
        or message.startswith("hi ")
        or message.startswith("hello ")
        or message.startswith("salam ")
        or message.startswith("hey ")
    ):
        answered_by_rules += 1
        print(
            f"{BOT_NAME}: Hello {customer_name}! Welcome to {BUSINESS_NAME}. "
            "Ask about our hours, menu, location, or type /quote."
        )

    # FAQ Intent 2: Opening hours
    elif "hour" in message or "open" in message or "close" in message or "timing" in message:
        answered_by_rules += 1
        print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")

    # FAQ Intent 3: Location / branch address
    elif "location" in message or "where" in message or "branch" in message or "shop" in message:
        answered_by_rules += 1
        print(f"{BOT_NAME}: We are located on Main Boulevard, Gulberg, Lahore.")

    # FAQ Intent 4: Delivery fees and policy
    elif "deliver" in message or "shipping" in message or "fee" in message or "charges" in message:
        answered_by_rules += 1
        print(
            f"{BOT_NAME}: Standard delivery is {DELIVERY_FEE:,} PKR, "
            f"and FREE on orders of {FREE_DELIVERY_LIMIT:,} PKR or more (after discount)!"
        )

    # FAQ Intent 5: Menu and prices
    elif "menu" in message or "price" in message or "items" in message or "cost" in message:
        answered_by_rules += 1
        print(
            f"{BOT_NAME}: Our menu: Cupcake ({CUPCAKE_PRICE:,} PKR), "
            f"Brownie ({BROWNIE_PRICE:,} PKR), Chocolate Cake ({CHOCOLATE_CAKE_PRICE:,} PKR). "
            "Type /quote for an exact price!"
        )

    # D. Smart fallback for anything the rules cannot answer
    else:
        unanswered_questions += 1

        # Clean with .capitalize() and slice to 150 characters to cap token cost
        clean_question = raw_input.strip().capitalize()[:150]
        estimated_tokens = round(len(clean_question) / 4)

        # WHY: Route messages containing personal data (phone, CNIC, address) to a local model
        # so sensitive customer details never leave the shop's computer and cost 0 PKR.
        if "phone" in message or "cnic" in message or "address" in message:
            chosen_model = "llama3.2 (local, private)"
            question_cost = 0.0
        else:
            chosen_model = "small cloud model (cheap)"
            question_cost = (estimated_tokens / 1000) * CLOUD_PRICE_PER_1K_TOKENS

        total_ai_cost += question_cost

        prompt = (
            f"     Prompt: You are the assistant of {BUSINESS_NAME}.\n"
            f"     Answer {customer_name} in 2 short lines. Question: {clean_question}"
        )

        print(f"{BOT_NAME}: Good question! Routed to: {chosen_model} (~{estimated_tokens} tokens)")
        print(prompt)

# E. Session report
print("\n" + "=" * 50)
print("Session report")
print(
    f"Messages: {total_messages} | Answered by rules: {answered_by_rules} | "
    f"Unanswered: {unanswered_questions} | Complaints: {complaint_count}"
)
print(f"Quotes: {total_quotes} | Quoted value: {total_quoted_value:,} PKR")
print(f"Estimated AI cost for unanswered questions: {total_ai_cost:.4f} PKR")
print("=" * 50)
