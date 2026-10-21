"""
Business Prompt Builder: Collects client business details and budget
via CLI inputs to generate a structured AI consultation prompt.
"""
name = input("What is your name? ")
business = input("What is your business type? ")
problem = input("What are problems you are facing? ")
budget = int(input("Monthly budget? "))

print(f"Welcome: {name}")
print(f"----Your Ai Prompt----")

# Inject user variables dynamically so the prompt adapts to any client without hardcoding

prompt = (
    f"Suggest 3 AI solutions for a {business} that struggles with {problem}. "
    f"Budget: {budget} PKR per month."
)
print(prompt)
