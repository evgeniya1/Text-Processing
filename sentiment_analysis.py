import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('twitter_samples')

analyzer = SentimentIntensityAnalyzer()

text1 = 'Hey, what a beautiful day! How amazing it is!'

print(text1)
print(analyzer.polarity_scores(text1))

tweets = list(nltk.corpus.twitter_samples.strings())
tweet1 = tweets[42]

print(tweet1)
print(analyzer.polarity_scores(tweet1))
