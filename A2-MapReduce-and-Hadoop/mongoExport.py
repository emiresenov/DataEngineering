import json

from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

db = client.tweets

collection = db.tweetsJSON


tweets = db.tweetsJSON.find({"retweeted_status":{"$exists":0}},{"_id":0, "text":1})

count = 0
f = open("mongoTweets.txt", "a")
for tweet in tweets:
    f.write(json.dumps(tweet))
    f.write("\n")
    count += 1

print("Tweets exported: ", count)

f.close()

client.close()


