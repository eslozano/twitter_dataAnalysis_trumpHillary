from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from pymongo import MongoClient
import json
import time

consumer_key = "p2UgQLNVDkCFAdvWsGELcyBhs"
consumer_secret = "BGCmkZvoSPuTghdKH1RrOO8lWP2VD76wv6lU05icoFvBVQQBOe"
access_token = "189954953-ibupX5R8qz2y6s1aIP7wqYW3tmWeMg6YzLj1tA5f"
access_token_secret = "SDWg9xaqswqgKDRELQ9w8uZzZktMLk15SXFmBCKTTfRoS"

client = MongoClient('localhost', 27017)
db = client['twitter_db']
collection = db['follow_usa_hillary_week2'] #Cambiar para los distintos estados

start_time = time.time() #grabs the system time

class StdOutListener(StreamListener):

    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            #print (tweet["id"])
            collection.insert(tweet)
            return True
        except BaseException, e:
            print ("ERROR %s"%(e))
            time.sleep(5)
            pass

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
	print (time.time())
	listener = StdOutListener(start_time)
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, listener)
	#[lng,lat,lng,lat ] El primer par es para la esquina inferior izquierda, el segundo la esquina superior derecha
	stream.filter(follow=['1339835893'],languages=['en'],locations=[-125.362778,25.557033,-67.300798,48.993829,-125.362778,25.557033,-67.300798,48.993829,-165.982207,52.469971,-141.147125,71.699910]) #Cambiar los locations y el track