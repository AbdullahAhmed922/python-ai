# Hallucination Hunt Results (Task 2.7 - Sweet Crumbs)

## Test Setup
- **Model:** `gemma3:4b` (with `temperature=0` and JSON schema enforcement)
- **Dataset:** 5 messy WhatsApp messages mixing English, Roman Urdu, off-menu requests (`pizza`), and general delivery questions.

## Observations & Findings
1. **Invented Customer Names on Anonymous Orders:** When testing a message without a name (e.g., *"2 brownies bhej dein Gulberg"*), the model sometimes filled `"customer"` with `"Customer"` or `"Ali"` to satisfy the schema. Our Python check (`customer.lower() not in msg.lower()`) caught and flagged this every time.
2. **Plural vs. Singular Item Names:** The model occasionally extracted `"cupcakes"` or `"brownies"` instead of `"cupcake"` or `"brownie"`. Adding a prompt instruction plus a Python singular normalization check (`name[:-1] in PRICES`) resolved false off-menu flags.
3. **Off-Menu Items:** In `"1 pizza and 2 brownies, Bilal, Model Town"`, the model extracted both items cleanly. Python's `name in PRICES` check priced the 2 brownies at 600 PKR and flagged `CHECK: 'pizza' is not on the menu`.
