# Our selected sample. Complex enough to exemplify each step
tweet = all_positive_tweets[2277]

# download the stopwords from NLTK
nltk.download('stopwords')
# -----------------------------------------------------------------------------------------------
import re                                  # Library for Regular Expression (RegEx) operations
import string                              # Library for String operations

from nltk.corpus import stopwords          # Module for stop - words that come with NLTK
from nltk.stem import PorterStemmer        # Module for Stemming
from nltk.tokenize import TweetTokenizer   # Module for Tokenizing strings

# Substitute (pattern,replacment,string origin)
# r'Raw data encapsulated here'
# Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
# [] Used to indicate a set of characters. In a set:
# \s Matches whitespace (spaces, tabs and new lines)
# + Causes the resulting RE to match 1 or more repetitions of the preceding RE.
data = re.sub(r'^RT[\s]+', '', tweet)

# Remove hyperlinks
# ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE.
data = re.sub(r'https?://[^\s\n\r]+', '', data)

# Remove hashtags by only removing the hash # sign from the word
data = re.sub(r'#', '', data)

# Instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

# tokenize tweets
data_tokens = tokenizer.tokenize(data)

#Import the english stop words list from NLTK
stopwords_english = stopwords.words('english') 

data_clean = []
for word in data_tokens: # Go through every word in your tokens list
    if (word not in stopwords_english and  # remove stopwords
        word not in string.punctuation):  # remove punctuation
        data_clean.append(word)
        
# Instantiate stemming class
stemmer = PorterStemmer()

# Create an empty list to store the stems
data_stem = []

for word in data_clean:
    stem_word = stemmer.stem(word)  # stemming word
    data_stem.append(stem_word)  # append to the list
