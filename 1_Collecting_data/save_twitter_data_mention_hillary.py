from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from pymongo import MongoClient
import json
import time

consumer_key = "QMUEe8PIdokPu6dlMQZBBCUgZ"
consumer_secret = "RmZXmeLbvfHFivtvw3c4YZUkAZxiQr1qrkdc3cKXS6Q5cK5Xs9"
access_token = "189954953-xfS2OdZdy6LyWSn5eXO7qpn0rSXgThBhDr6Ic5nI"
access_token_secret = "Zy2NRrK4O0F311edpifwC9t8I02wOxf58zLakWNI6c6tF"

client = MongoClient('localhost', 27017)
db = client['twitter_db']
collection = db['mention_usa_hillary_week2'] #Cambiar para los distintos estados

start_time = time.time() #grabs the system time
keyword_list = ['twitter'] #track list

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
	stream.filter(track=['Hillary','Clinton','HillaryClinton','Hillary2016','ImWither'],languages=['en'],locations=[-125.362778,25.557033,-67.300798,48.993829,-125.362778,25.557033,-67.300798,48.993829,-165.982207,52.469971,-141.147125,71.699910]) #Cambiar los locations y el track