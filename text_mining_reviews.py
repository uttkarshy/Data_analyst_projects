import requests
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
response = requests.get('https://api.openbrewerydb.org/breweries')
breweries = response.json()

reviews = []
for brewery in breweries:
    if 'reviews' in brewery:
        reviews += brewery['reviews']
stop_words = set(stopwords.words('english'))

words = []
for review in reviews:
    tokens = word_tokenize(review.lower())
    words += [token for token in tokens if token.isalpha() and token not in stop_words]
blob = TextBlob(' '.join(words))

sentiment = blob.sentiment.polarity
keywords = blob.word_counts.items()
most_common_keywords = sorted(keywords, key=lambda x: x[1], reverse=True)[:10]
