from textblob import TextBlob

history = []
stats = {
    "positive": 0,
    "negative": 0,
    "neutral": 0
}

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, polarity

def show_stats():
    print("\n Sentiment Statistics")
    print(f"Positive: {stats['positive']}")
    print(f"Negative: {stats['negative']}")
    print(f"Neutral: {stats['neutral']}\n")

def show_history():
    print("\n Conversation History")
    for i, (text, sentiment, polarity) in enumerate(history, 1):
        print(f"{i}. {text} → {sentiment} ({polarity:.2f})")
    print()

def reset_data():
    history.clear()
    stats["positive"] = 0
    stats["negative"] = 0
    stats["neutral"] = 0
    print("\n Data has been reset!\n")

def final_report():
    print("\n FINAL REPORT")
    print("=" * 30)
    show_stats()
    print(f"Total messages analyzed: {len(history)}")
    print("Thanks for using the chatbot!")

def chatbot():
    print(" Sentiment Chatbot Started!")
    print("Type a message to analyze sentiment.")
    print("Commands: stats, history, reset, quit\n")

    while True:
        user_input = input("How are you doing today? ").strip().lower()

        if user_input == "quit":
            final_report()
            break

        elif user_input == "stats":
            show_stats()

        elif user_input == "history":
            show_history()

        elif user_input == "reset":
            reset_data()

        else:
            sentiment, polarity = analyze_sentiment(user_input)

            history.append((user_input, sentiment, polarity))
            stats[sentiment] += 1

            print(f"Bot: This message is {sentiment} (score: {polarity:.2f})\n")

if __name__ == "__main__":
    chatbot()