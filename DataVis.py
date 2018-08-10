'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

from wordcloud import WordCloud

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib.pyplot as blt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []

for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    polarity.append(tb.polarity)
    print("[] Added Polarity in the list...\n")
    subjectivity.append(tb.subjectivity)
    print("[] Added Subjectivity in the list...\n")

# Textblob sample:
average_polarity = 0

for pol in polarity:
    average_polarity += pol

print(polarity)
average_polarity =  average_polarity/len(polarity)
print(average_polarity)
print(subjectivity)

#someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18, 0.25]
plt.hist(polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

blt.hist(subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
blt.xlabel('Values')
blt.ylabel('Number of Items')
blt.title('Histogram of Numbers')
blt.axis([-1.1, 1.1, 0, 100])
blt.grid(True)
blt.show()

# PART 3
allTweets = ""
for tweet in tweetData:
    allTweets += tweet["text"]

allTweets_textblob = TextBlob(allTweets)

wordsToFilter = ["the","but","and","for","http","about","cloud","in"]

filteredDictionary = dict()

for word in allTweets_textblob.words:
    if word.lower() in wordsToFilter:
        continue
    if len(word) < 3:
        continue
    if not word.isalpha():
        continue
    filteredDictionary[word.lower()] = allTweets_textblob.word_counts[word.lower()]

wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()

# the_count = allTweets_textblob.word_counts['the']

# filteredWords = {}
#
# for item in allTweets_textblob:
#     if (allTweets_textblob.words_counts[item] > 3):
#         filteredWords[item] = allTweets_textblob.words_counts[item]
#
# print(the_count) # prints the number of 'the's from all the tweets
# >> TextBlob returns list of lists? sublists are lists of words in a single tweet?
