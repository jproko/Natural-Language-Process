import nltk                             # Python Library for Natural Language Processing 
from nltk.corpus import twitter_samples # NLTK twitter dataset
#-----------------------------------------------------------------------------------------
import matplotlib.pyplot as plt         # Matlab Python Library for visualization purposes
import random                           # Pseudo Random Number Generator
#-----------------------------------------------------------------------------------------
# downloads sample twitter dataset.
nltk.download('twitter_samples')
#-----------------------------------------------------------------------------------------
#select the set of positive and negative tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')
#-----------------------------------------------------------------------------------------
# display the length of all positive tweets
print('Number of positive tweets: ', len(all_positive_tweets))
# display the length of all negative tweets
print('Number of negative tweets: ', len(all_negative_tweets))
#-----------------------------------------------------------------------------------------
# Declare a figure with a custom size
# Input : (float,float) representing width and height in inches (1 inch = 2.54 cm)
fig = plt.figure(figsize=(4, 4))

# Labels for the two classes
labels = 'Positive Sentiment Tweets', 'Negative Sentiment Tweets'

# Sizes for each slide
sizes = [len(all_positive_tweets), len(all_negative_tweets)] 

# Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
# Input:
#     sizes: the wedge sizes
#     labels: the labels
#     autopct: A string or function used to label the wedges with their numeric value. 
#              The label will be placed inside the wedge. 
#              If it is a format string, the label will be fmt % pct. 
#              If it is a function, it will be called.
#     shadow: Draw a shadow beneath the pie.
#     startangle: The angle by which the start of the pie is rotated, counterclockwise from the x-axis.
plt.pie(sizes, labels=labels, autopct='%.2f', shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Display the chart
plt.show()
#-----------------------------------------------------------------------------------------
# Print positive in greeen
print('\033[92m' + all_positive_tweets[random.randint(0,4999)])
print('\033[92m' + all_positive_tweets[random.randint(0,4999)])
print('\033[92m' + all_positive_tweets[random.randint(0,4999)])
print('\033[92m' + all_positive_tweets[random.randint(0,4999)])
print('\033[92m' + all_positive_tweets[random.randint(0,4999)] + '\n')

# print negative in red
print('\033[91m' + all_negative_tweets[random.randint(0,4999)])
print('\033[91m' + all_negative_tweets[random.randint(0,4999)])
print('\033[91m' + all_negative_tweets[random.randint(0,4999)])
print('\033[91m' + all_negative_tweets[random.randint(0,4999)])
print('\033[91m' + all_negative_tweets[random.randint(0,4999)])
