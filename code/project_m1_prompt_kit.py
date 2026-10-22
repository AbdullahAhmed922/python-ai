business_name = input("What is your business name?: ")
business_type = input("What is your business type?: ")
city = input("What is your city?: ")
main_customers = input("Who are your main customers?: ")
monthly_budget = input("What is your monthly budget?: ")

print("*" * 41)
print(f"AI Prompt Kit for {business_name}".center(41))
print("*" * 41)

print("[1] Marketing")
print(f"Write a short Instagram post for {business_name}, a {business_type} in {city}. Target {main_customers}. Friendly tone, 1 call to action.")
print()

print("[2] Customer Service")
print(f"You are the manager of {business_name}. Write a polite reply to a customer whose order arrived late. Apologise and offer a small discount.")
print()

print("[3] Growth")
print(f"Suggest 3 low-cost AI tools a {business_type} in {city} can use to attract {main_customers} with a budget of {monthly_budget} PKR per month.")
