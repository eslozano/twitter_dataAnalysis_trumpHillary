from pymongo import MongoClient
import csv
import tweepy

client = MongoClient()
db = client.twitter_db
collection = db.follow_usa_hillary.find()

#cursor = db.restaurants.find({"lang": "es"})


with open('grafo.csv', 'wb') as csvfileNodes:
	fieldnames = ['date', 'id_source','latitud','longitud','retweet_by','retweet_to']
	writer = csv.DictWriter(csvfileNodes, fieldnames=fieldnames)
	for document in collection:	
		retweet_by=""
		if document['retweeted_status']:
			retweet_by=document['user']['screen_name'].encode("utf-8")
			retweet_to=document['retweeted_status']['user']['screen_name'].encode("utf-8")
			id_source=document['retweeted_status']['id_str']
			date=(datetime.datetime.strptime(document['created_at'],'%a %b %d %H:%M:%S +0000 %Y').datetime()
			lon = (float(document['place']['bounding_box']['coordinates'][0][0][0] - document['place']['bounding_box']['coordinates'][0][2][0]) / 2 ) + float(document['place']['bounding_box']['coordinates'][0][2][0])
            lat = (float(document['place']['bounding_box']['coordinates'][0][0][1] + document['place']['bounding_box']['coordinates'][0][2][1]) / 2 ) + float(document['place']['bounding_box']['coordinates'][0][2][1])
			writer.writerow({ 'date': date,'id_source': id_source,'latitud': lat,'longitud':lon,'retweet_by':retweet_by,'retweet_to':retweet_to})
			db.collection.remove( { id_str:document['id_str'] })

