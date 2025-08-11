import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def detect_rudeness(player_input):
    """
    Returns True if input is likely rude/negative.
    Adjust the threshold if too sensitive.
    """
    scores = sia.polarity_scores(player_input)
    return scores['compound'] < -0.5

def detect_apology(player_input):
    """
    Returns True if the player is apologizing.
    Add/remove keywords as needed.
    """
    apology_keywords = ['sorry', 'apologize', 'forgive', 'my bad']
    return any(word in player_input.lower() for word in apology_keywords)


def get_sentiment_label(player_input):
    scores = sia.polarity_scores(player_input)
    compound = scores['compound']
    if compound > 0.5:
        return 'positive'
    elif compound < -0.5:
        return 'negative'
    else:
        return 'neutral'
