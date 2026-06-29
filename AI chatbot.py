print("Welcome to the Chatbot!")
name = input("What is your name? \n")
print("Hello,", name)
while True:
    mood = input("How are you feeling today? (good/bad/neutral): ").lower().strip()
    if mood == "good":
        print("I'm glad you're feeling good.")
    elif mood == "bad":
        print("I'm sorry to hear that. I hope your day gets better and try to something that brings you joy.")
    elif mood == "neutral":
        print("I hope you have a nice day.")
    else:
        print("I don't understand that response.")

    hobby = input("What is your favourite hobby or activity? ")
    print("That sounds interesting.")

    answer = input("Would you like to continue chatting? (yes/no): ").lower().strip()

    if answer != "yes":
        print("Goodbye,", name)
        break