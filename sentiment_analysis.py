import spacy  # importing spacy
import pandas as pd
from textblob import TextBlob
from detokenize.detokenizer import detokenize

nlp = spacy.load('en_core_web_md')

def process_input(text):
   # Remove missing values from column
    tempdf=pd.DataFrame(columns=[text]).dropna()
    # Preprocess the text with spaCy
    doc = nlp(str(tempdf))

    # Perform cleaning actions
    clean_token = []
    clean_token = [ ((token.text).lower().strip('.\n,: ')) for token in doc if not (token.is_stop)]   
    sentence = detokenize(clean_token)

    return sentence


def process_output(sentence): 
    # Cleaned sentence  
    print(sentence ) 
    blob = TextBlob(sentence)

    # Determine sentiment
    polarity = blob.sentiment.polarity   
    return polarity


def analyze_polarity(text):
    sentence = process_input(text)
    polarity = process_output(sentence)
    return polarity


# Read in text data
df = pd.read_csv("amazon_product_reviews.csv")

# Retrieve 'reviews.text' column
reviews_data = df['reviews.text']
print(reviews_data.head())
 
test_data = reviews_data[0]
polarity_score = analyze_polarity(test_data)

# Assign polarity score
if polarity_score > 0:
    sentiment = 'positive'
elif polarity_score < 0:
    sentiment = 'negative'
else:
    sentiment = 'neutral'
 
print(f"Text: {test_data}\nPolarity score: {polarity_score}\nSentiment: {sentiment}")

# Similarity review
first_review = nlp(reviews_data[0])
second_review = nlp(reviews_data[14])

print("Reviews : ")
print(first_review.similarity(second_review))

# The reviews appear to be reasonably similar

 