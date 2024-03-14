# finalCapstone

sentiment_analysis.py

Sentiment analysis allows us to detect the emotion behind a piece of text using Natural Language Processing
In this project we implement a sentiment analysis model using spaCy
This involves preprocessing the text data, removing stopwords, and performing any necessary text cleaning to prepare the reviews for analysis

Sentiment_analysis_report

The .polarity attribute can be used to measure the strength of the
sentiment in a product review. A polarity score of 1 indicates a very positive
sentiment, while a polarity score of -1 indicates a very negative sentiment. A
polarity score of 0 indicates a neutral sentiment

The dataset contains buyer evaluations of Kindles they have purchased
The dataset has been processed by removing stopwords, missing values, several punctuations and converting to lowercase
Several instances have been run, and the processed dataset, the full text and the polarity score shown

kindle light easy use especially beach!!!
Text: This kindle is light and easy to use especially at the beach!!!
Polarity score: 0.2777777777777778
Sentiment: positive

super excited gift super convenient best buy echo products store instead having purchase amazon
Text: Super excited to give this as a gift. It's super convenient that Best Buy has Echo products in store instead of having to purchase from Amazon.
Polarity score: 0.5104166666666666
Sentiment: positive

purchased gift absolutely loved
Text: This was purchased as a gift and they've absolutely loved it.
Polarity score: 0.7
Sentiment: positive

bought mother law buying
Text: We bought this for mother in law, buying another for me.
Polarity score: 0.0
Sentiment: neutral

thought big small paper turn like palm think small read comfortable regular kindle definitely recommend paperwhite instead
Text: I thought it would be as big as small paper but turn out to be just like my palm. I think it is too small to read on it... not very comfortable as regular Kindle. Would definitely recommend a paperwhite instead.
Polarity score: -0.016666666666666663
Sentiment: negative

Instructions for Use 
Download a dataset of product reviews: Consumer Reviews of AmazonProducts. You can save it as a CSV file, naming it:
amazon_product_reviews.csv.  Ensure it is held in the same folder as the code

Screenshots of the project in action.
![StanWareing/finalCapstone/assets/36082046/8172d4af-25f2-436c-b173-74bb1354514b)]
![image[Doc2.docx](https://github.com/StanWareing/finalCapstone/files/14603769/Doc2.docx)
](https://github.com/StanWareing/finalCapstone/assets/36082046/54b1be13-a113-49dc-b71f-e85f249c29bd)

The similarity() function is used to compare the similarity of two
product reviews. A similarity score of 1 indicates that the two reviews are
more similar, while a similarity score of 0 indicates that the two reviews are
not similar.

SpaCy is able to compare two objects and make a prediction of how similar they
are. Let’s begin by using simple examples to understand how SpaCy categorises
similar and dissimilar objects. The similarity is shown as a floating decimal from 0
to 1, where 0 indicates ‘most dissimilar’ and the strength of the similarity increases
all the way up to 1.

The program has been run comparing 2 sentences, and the otput of 0.85 ( rounded ) shows they are quite similar




 




 
