from datetime import datetime

weather_keywords = ["weather", "rain", "sunny", "forecast"]
news_keywords = ["news", "headlines", "update"]
time_keywords = ["time", "clock", "date"]
good_keywords = ["good", "great", "happy", "fine"]
bad_keywords = ["bad", "sad", "upset", "angry"]
neutral_keywords = ["okay", "ok", "neutral", "alright"]

print("Welcome to the Chatbot!")

name = input("What is your name? ")
print("Hello,", name)

while True:
    message = input("\nWhat would you like to talk about, Weather?, News?, Time? ").lower().strip()

    if any(word in message for word in good_keywords):
        print("I'm glad you're feeling good.")

    elif any(word in message for word in bad_keywords):
        print("I'm sorry to hear that. I hope things get better.")

    elif any(word in message for word in neutral_keywords):
        print("I hope you have a nice day.")

    elif any(word in message for word in weather_keywords):
        print("The weather is sunny with a chance of rain later today.") 

    elif any(word in message for word in news_keywords):
        print("Today's news: Scientists continue making exciting discoveries.")

    elif any(word in message for word in time_keywords):
        current = datetime.now()
        print("Current date:", current.strftime("%d/%m/%Y"))
        print("Current time:", current.strftime("%I:%M %p"))

    elif "hobby" in message or "sport" in message:
        hobby = input("What is your favourite hobby or sport? ")
        print("That sounds interesting.")

    else:
        print("I'm not sure how to respond to that.")

    answer = input("\nWould you like to continue chatting? (yes/no): ").lower().strip()

    if answer != "yes":
        print("Goodbye,", name)
        break