"""
Task 1.8: Business Helper Bot (Module 1 Final)
An interactive customer support chatbot for a local computer shop that handles FAQs, complaints, and fallbacks.
"""

print("TechFix Bot: Hi! Ask about timings, fees, location or repairs. Type 'bye' to exit.")

# Why: Asking the name once before the loop avoids annoying the customer by asking their name on every turn.
raw_user_name = input("TechFix Bot: What is your name? ")
user_name = raw_user_name.strip().title()

message_count = 0
unanswered_count = 0
complaint_count = 0

while True:
    raw_msg = input(f"{user_name}: ")
    # Why: Cleaning every message makes keyword detection case-insensitive and immune to accidental spaces.
    msg = raw_msg.strip().lower()

    if msg == "bye":
        print(f"TechFix Bot: Take care, {user_name}!")
        break

    # Stretch Goal: Immediate exit to human agent
    if "agent" in msg or "human" in msg:
        message_count += 1
        print("TechFix Bot: Connecting you to a human...")
        break

    message_count += 1

    # Why: Checking complaints first ensures frustrated users aren't given a generic FAQ response when they mention a keyword like "fee" or "time" inside a complaint.
    if "late" in msg or "complaint" in msg or "bad" in msg or "broken" in msg:
        complaint_count += 1
        print(f"TechFix Bot: Sorry about that, {user_name}. Our shop manager will call you today.")
    elif msg == "hi" or msg == "hello" or msg.startswith("hi ") or msg.startswith("salam"):
        print(f"TechFix Bot: Walaikum Assalam, {user_name}! How can I help you with your laptop today?")
    elif "timing" in msg or "time" in msg or "open" in msg or "hours" in msg:
        print("TechFix Bot: We are open 11 am to 9 pm, Monday to Saturday.")
    elif "fee" in msg or "price" in msg or "cost" in msg or "charges" in msg:
        print("TechFix Bot: Basic diagnostic and cleaning fee is 1,500 PKR.")
    elif "location" in msg or "address" in msg or "where" in msg:
        print("TechFix Bot: We are on the 2nd Floor, Hafeez Center, Gulberg III, Lahore.")
    elif "appointment" in msg or "book" in msg or "repair" in msg or "upgrade" in msg:
        print(f"TechFix Bot: Sure, {user_name}! Share your laptop model and we will book a repair slot for you.")
    else:
        unanswered_count += 1
        print(
            f"TechFix Bot: I am not sure yet. In Module 2, an AI will answer: "
            f"You are the friendly assistant of TechFix Laptop Care. Answer in 2 lines: {raw_msg.strip()}"
        )

print("========================================")
print(f"Chat summary: {message_count} messages, {unanswered_count} unanswered, {complaint_count} complaints.")
