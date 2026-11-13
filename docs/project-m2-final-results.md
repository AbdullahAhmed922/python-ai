# Module 2 Final Project: AI Quality Test Results (`Sweet Crumbs`)

## 1. Two Agent Cases Where the AI Nearly Made a Mistake

### Agent Case 1: Plural Item Names in Tool Calls (`"I want 2 brownies"`)
- **What happened:** When the user typed `"I am Ali, I want 2 brownies"`, `llama3.2:1b` called `place_order({'item': 'brownies', 'quantity': 2, 'customer': 'Ali'})` with a plural string `"brownies"`, which did not directly match the singular dictionary key `"brownie"` in `business.json`.
- **What my code caught:** Our helper `normalize_item(item, PRICES)` strips trailing `"s"` and converts `"ies"` -> `"y"` (`"brownies"` -> `"brownie"`, `"cupcakes"` -> `"cupcake"`) before checking `PRICES`, so valid orders never fail due to pluralization.

### Agent Case 2: Ordering Without Giving a Customer Name (`"Order 3 cupcakes please"`)
- **What happened:** When a user asked to place an order without stating their name, the model tried calling `place_order(item="cupcake", quantity=3, customer="Unknown")` or `customer="Customer"`.
- **What my code caught:** Inside `place_order`, we added a guardrail checking `if not clean_customer or clean_customer.lower() in ("unknown", "customer", "none"):` which returns `"Cannot place order: please ask the customer for their name first."` without prompting the owner or saving a nameless order.

---

## 2. Two WhatsApp `/import` Cases Where the AI Made a Mistake

### Import Case 1: Invented Customer Name (`"1 pizza and 2 brownies, Model Town"`)
- **What happened:** On a message with an address (`Model Town`) and no person's name, the LLM occasionally filled the `customer` field with a guessed name like `"Ahmed"` or `"Model Town"`.
- **What my code caught:** Our verification check `elif customer.lower() not in raw_msg.lower():` flagged `CHECK: customer 'Ahmed' is not in the message (invented?)` and printed `'pizza' is not on the menu`, allowing the owner to type `no` at the approval prompt.

### Import Case 2: Off-Menu Item Included in Extraction (`"1 pizza and 2 brownies"`)
- **What happened:** The extractor included `{"name": "pizza", "quantity": 1}` in the JSON `items` array because `"1 pizza"` looks like a food order item in natural language.
- **What my code caught:** The loop checks `if norm_name not in PRICES:` before calculating any totals. It printed `CHECK: 'pizza' is not on the menu` and excluded pizza from `valid_items`, so `calculate_total()` billed only the 2 brownies (`600 PKR`).

---

## 3. Docstring & Code Fix That Improved Accuracy

- **The Problem:** Initially, when customers asked `"What are your timings?"` or `"Where is your shop located?"`, the agent either passed `topic="timings"` or `topic="location"` to `get_info`, which didn't match the exact keys `"hours"` and `"address"` in `business.json`.
- **The Fix:**
  1. Updated the `get_info` docstring `Args:` description to explicitly list the exact keys: `topic: The information topic to check (hours, delivery, city, address, contact, type, or name).`
  2. Added an `aliases` dictionary inside `get_info()` mapping `"timing"`, `"timings"`, `"opening hours"` -> `"hours"` and `"location"`, `"where"` -> `"address"`. After this fix, every timing and location query resolved on the first tool call.
