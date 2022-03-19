import re                                  # Library for Regular Expression (RegEx) operations
import string                              # Library for String operations
import random                              # Python library to generate a pseudo - random integer
import matplotlib.pyplot as plt            # Visualization library
import numpy as np                         # Library for scientific computing and matrix operations

import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # Sample Twitter dataset from NLTK
from nltk.corpus import stopwords          # Module for stop - words that come with NLTK
from nltk.stem import PorterStemmer        # Module for Stemming
from nltk.tokenize import TweetTokenizer   # Module for Tokenizing strings

# ============== PRE - PROCESS FUNCTION ==============
def preProcess_tweet(tweet):
    # Part 1: Clean redundancy
    # ------------------------
    # Remove re-tweets
    data = re.sub(r'^RT[\s]+', '', tweet)
    
    # Remove hyperlinks
    data = re.sub(r'https?://[^\s\n\r]+', '', data)
    
    # Remove hashtags by only removing the hash # sign from the word
    data = re.sub(r'#', '', data)
    
    # Part 2: Tokenize
    # ------------------------
    # Instantiate tokenizer class
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    
    # tokenize tweets
    data_tokens = tokenizer.tokenize(data)
    
    data_clean = []
    for word in data_tokens: # Go through every word in your tokens list
        if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
            data_clean.append(word)
    
    # Part 3: Stem
    # ------------------------
    # Instantiate stemming class
    stemmer = PorterStemmer()

    # Create an empty list to store the stems
    data_stem = []

    for word in data_clean:
        stem_word = stemmer.stem(word)  # stemming word
        data_stem.append(stem_word)  # append to the list
        
    return data_stem
# ============== BUILD FREQUENCIES FUNCTION ==============
def build_freqs(tweets_dataset, ylabels):
    
    # Convert np array to list since zip needs an iterable.
    # The squeeze is necessary or the list ends up with one element.
    # Also note that this is just a NOP if ys is already a list.
    ylabelslist = np.squeeze(ylabels).tolist()

    # Start with an empty dictionary and populate it by looping over all tweets
    # and over all processed words in each tweet.
    freqs = {}
    for y, tweet in zip(ylabelslist, tweets_dataset):
        for token in preProcess_tweet(tweet):
            pair = (token, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1

    return freqs
# ============== MAIN CODE HERE ==============
# -------------- LOADING DATA --------------
# download the samples from NLTK
nltk.download('twitter_samples')

# download the stopwords from NLTK
nltk.download('stopwords')

# Select the set of positive and negative tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

# Import the english stop words list from NLTK
stopwords_english = stopwords.words('english')

# -------------- GENERATING FREQUENCIES --------------
freqs = build_freqs(tweets,labels)
# Select some words to appear in the report. We will assume that each word is unique (i.e. no duplicates)
keys = ['happi', 'merri', 'nice', 'good', 'bad', 'sad', 'mad', 'best', 'pretti',
        '❤', ':)', ':(', '😒', '😬', '😄', '😍', '♛',
        'song', 'idea', 'power', 'play', 'magnific']

# -------------- GENERATING FREQUENCY LIST --------------
# List representing our table of word counts.
# Each element of data list, consist of a sublist with this pattern: 
#     [<word>, <positive_count>, <negative_count>]
data = []

# loop through our selected words
for token in keys:
    
    # Initialize positive and negative counts
    pos = 0
    neg = 0
    
    # Retrieve number of positive counts
    # If token exists as a positively indexed token in our frequencies dictionary
    if (token, 1.0) in freqs:
        pos = freqs[(token, 1.0)]
    else:
        pos = 0
        
    # retrieve number of negative counts
    # If token exists as a positively indexed token in our frequencies dictionary
    if (token, 0.0) in freqs:
        neg = freqs[(token, 0.0)]
    else:
        neg = 0
        
    # append the word counts to the table
    data.append([token, pos, neg])
    
# -------------- VISUALIZING --------------    
fig, ax = plt.subplots(figsize = (10, 10))

# convert positive raw counts to logarithmic scale. we add 1 to avoid log(0)
x = np.log([x[1] + 1 for x in data])  

# do the same for the negative counts
y = np.log([x[2] + 1 for x in data]) 

# Plot a dot for each pair of words
ax.scatter(x, y)  

# assign axis labels
plt.xlabel("Log Positive count")
plt.ylabel("Log Negative count")

# Add the word as the label at the same position as you added the points just before
for i in range(0, len(data)):
    ax.annotate(data[i][0], (x[i], y[i]), fontsize=12)

ax.plot([0, 9], [0, 9], color = 'red') # Plot the red line that divides the 2 areas.
plt.show()
