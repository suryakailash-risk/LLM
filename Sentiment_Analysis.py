from transformers import pipeline
sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to analyze sentiment of given text
def analyze_sentiment(text):
    response = sentiment(text)
    sentiment_score = response[0]['score']
    sentiment_label = response[0]['label']
    return sentiment_label, sentiment_score 

# Main function to handle user input and run sentiment analysis interactively
def main():
    while True:
        user_input = input("Enter text for sentiment analysis (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting sentiment analysis.")
            break
        sentiment_label, sentiment_score = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment_label}, Score: {sentiment_score:.2f}")
main()
