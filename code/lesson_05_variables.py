"""
Task 1.5: AI Model Profile Card
Displays a technical profile card for an AI model and estimates chat and monthly token costs.
"""

# Why: Storing the core configuration in typed variables makes it easy to update model specs in one place.
model_name = "gemma3:4b"
context_window = 128000
price_per_1k = 0.5
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k} PKR {type(price_per_1k)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")
print()

# Why: input() always returns a string, so we convert it to int() to perform mathematical cost calculations.
tokens_per_chat = int(input("Tokens per chat: "))

estimated_cost = round((tokens_per_chat / 1000) * price_per_1k, 2)
print(f"Estimated cost: {estimated_cost} PKR")

# Stretch Goal: Monthly cost calculation
chats_per_day = int(input("Chats per day: "))
monthly_cost = round(estimated_cost * chats_per_day * 30, 2)
print(f"Estimated monthly cost (30 days): {monthly_cost} PKR")
