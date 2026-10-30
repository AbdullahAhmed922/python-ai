"""
Task 1.7: Smart Model Router
Routes tasks to the right AI model based on privacy, complexity, and cost while enforcing token limits.
"""

# Why: Normalizing with .strip().lower() ensures inputs like " Code " or "PRIVATE" still match our conditions.
task_type = input("Task (code / private / chat): ").strip().lower()
estimated_tokens = int(input("Estimated tokens: "))
is_paid = input("Is this a paid user? (yes/no): ").strip().lower()

# Why: Routing by task balances privacy (local Ollama), capability (Claude for code), and low cost (cheap chat model).
if task_type == "code":
    chosen_model = "claude (cloud, strong at code)"
    price_per_1k = 0.80
elif task_type == "private":
    chosen_model = "llama3.2 (local, Ollama)"
    price_per_1k = 0.00
else:
    chosen_model = "gemma3 (cloud, fast & cheap)"
    price_per_1k = 0.20

if estimated_tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# Stretch Goal: Check free user limits using 'and'
if is_paid == "no" and estimated_tokens > 2000:
    print("Upgrade to send long requests.")

estimated_cost = (estimated_tokens / 1000) * price_per_1k

print(f"Chosen model: {chosen_model}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")
