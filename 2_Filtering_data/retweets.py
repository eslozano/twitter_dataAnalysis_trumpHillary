from pymongo import MongoClient
import csv
import tweepy

def calcularCoordenadas(document):
	x0=float(document['place']['bounding_box']['coordinates'][0][2][0])
	x1=float(document['place']['bounding_box']['coordinates'][0][0][0])
	y0=float(document['place']['bounding_box']['coordinates'][0][0][1])
	y1=float(document['place']['bounding_box']['coordinates'][0][1][1])
	return (x1-x0)/2+x0,(y1-y0)/2+y0 #Retorna long,latit

client = MongoClient()
db = client.twitter_db
collection = db.follow_usa_hillary.find()

with open('grafo.csv', 'wb') as csvfileNodes:
	fieldnames = ['date', 'id_source','latitud','longitud','type_location',
		'latitud_source','longitud_source','type_location_source',
		'likes','retweets','retweet_by','retweet_to',
		'text_len','text_count_hashtags','text_count_symbols','text_count_urls','text_count_mentions','text']
	writer = csv.DictWriter(csvfileNodes, fieldnames=fieldnames)
	writer.writeHeader()

	for document in collection:
		if document['retweeted_status']:
			if 'entities' in document:
				user_mentions=document['retweeted_status']['entities']['user_mentions']
				if any(u['screen_name'] == 'HillaryClinton' for u in user_mentions) or any(u['screen_name'] == 'realDonaldTrump' for u in user_mentions):
					retweet_by=document['user']['screen_name'].encode("utf-8")
					retweet_to=document['retweeted_status']['user']['screen_name'].encode("utf-8")
					id_source=document['retweeted_status']['id_str']
					date=(datetime.datetime.strptime(document['created_at'],'%a %b %d %H:%M:%S +0000 %Y')).strftime("%d/%m/%Y %H:%M")
					
					lon=None
					lat=None
					type_location=None
					if document['coordinates'] != None:
						if document['coordinates']['type'] == "Point":
							lon=document['coordinates']['coordinates'][0]
							lat=document['coordinates']['coordinates'][1]
							type_location="coordinates"
					elif document['place'] != None:
						lon,lat=calcularCoordenadas(document)
						type_location="place"

					lon_source=None
					lat_source=None
					type_location_source=None
					if document['retweeted_status']['coordinates'] != None:
						if document['retweeted_status']['coordinates']['type'] == "Point":
							lon_source=document['retweeted_status']['coordinates']['coordinates'][0]
							lat_source=document['retweeted_status']['coordinates']['coordinates'][1]
							type_location_source="coordinates"
					elif document['retweeted_status']['place'] != None:
						lon_source,lat_source=calcularCoordenadas(document['retweeted_status'])
						type_location_source="place"

					text_chash=len(document['retweeted_status']['entities']['hashtags'])
					text_csymbols=len(document['retweeted_status']['entities']['symbols'])
					text_curls=len(document['retweeted_status']['entities']['urls'])
					text_cment=len(document['retweeted_status']['entities']['user_mentions'])

					writer.writerow({ 'date': date,'id_source': id_source,
						'latitud': lat,'longitud':lon,'type_location':type_location,
						'latitud_source': lat_source,'longitud_source':lon_source,'type_location_source':type_location_source,
						'likes':document['retweeted_status']['favorite_count'],
						'retweets':document['retweeted_status']['retweet_count'],
						'retweet_by':retweet_by,'retweet_to':retweet_to,
						'text_len':len(document['retweeted_status']['text']),'text_count_hashtags':text_chash,'text_count_symbols':text_csymbols,
						'text_count_urls':text_curls,'text_count_mentions':text_cment,
						'text':document['retweeted_status']['text'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' ')})
					#db.collection.remove( { id_str:document['id_str'] })
