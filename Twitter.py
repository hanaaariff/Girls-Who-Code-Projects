import json


tweetFile = open("tweets_small.json","r")
tweetData = json.load(tweetFile)
tweetFile.close()

print(tweetData[0]["id"])

print(tweetData[0]["text"])

for index in range(len(tweetData)):
    print("[Tweet Data] " + str(index) + " : " + tweetData[index]["text"] + "\n")

for tweet in tweetData:
    print("[Tweet Data]: " + tweet["text"] + "\n")
