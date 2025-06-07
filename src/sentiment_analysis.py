from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Load your cleaned CSV
df = pd.read_csv('./data/raw/bank_reviews_cleaned.csv')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis
df['sentiment'] = df['review'].astype(str).apply(get_sentiment)

# Save updated CSV
df.to_csv('./data/processed/bank_reviews_with_sentiment.csv', index=False)

print("✅ Sentiment analysis complete. Results saved to 'bank_reviews_with_sentiment.csv'.")
