import pymongo
import json

from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

db = client.tweets
collection = db.tweetsJSON

for i in range(20):
    doc = "tweets_" + str(i) + ".txt"
    f = open(doc, "r")
    for x in f:
        try:
            tweet = json.loads(x)
            try:
                collection.insert_one(tweet)
            except:
                print("Somethings went wrong")
        except:
            continue


client.close()



