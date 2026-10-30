"""
Task 1.6: Prompt Cleaner
Sanitizes user input, estimates token usage and cost, checks keywords, and constructs a safely sized AI prompt.
"""

name = input("Enter your name: ")
question = input("What is your question? ")

# Why: Stripping outer whitespace and normalizing capitalization prevents messy formatting inside the AI prompt.
clean_name = name.strip().title()
clean_question = question.strip().capitalize()

# Stretch Goal: Filter out inappropriate words before measuring or sending to the model
clean_question = clean_question.replace("stupid", "***").replace("Stupid", "***")

char_count = len(clean_question)
estimated_tokens = round(char_count / 4)
mention_python = "python" in clean_question.lower()

# Stretch Goal: Calculate example cost (assuming 0.5 PKR per 1K tokens)
estimated_cost = (estimated_tokens / 1000) * 0.5

print("========================================")
print(f"Cleaned Name: {clean_name}")
print(f"Cleaned Question: {clean_question}")
print(f"Characters: {char_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mention_python}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")
print("========================================")

# Why: Slicing to [:150] enforces a strict character limit so long inputs cannot unexpectedly spike token costs.
prompt = f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {clean_question[:150]}"""

print(prompt)
