#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script para poder almacenar en un csv los siguientes datos de los Tweets que no sean Retweets
y que contengan mentions @HillaryClinton y/o @RealDonaldTrump
id_Tweet: Id del tweet
datetime_creation: Fecha completa con hora y fecha
date_creation: El dia, mes, año en el que fue creado el tweet
time_creation: La banda horaria en la que fue creado (del 0 al 23)
latitud: Del campo coordinates o del bounding box
longitud: Del campo coordinates o del bounding box
type_location: coordinates | place | None
country_code: Codigo del pais
country: Nombre del pais
mention_candidate: @realDonaldTrump | @HillaryClinton | both
screen_name: El nombre del usuario que hizo el tweet
account_age_year: El año en el que se creo la cuenta
account_age_month: El mes en el que se creo la cuenta
user_location: La localidad que un usuario ha completado en su perfil
lang: Idioma del tweet
source: Plataforma de twitter desde donde fue publicado el tweet
text_len,text_count_hashtags,text_count_symbols,text_count_urls,text_count_mentions: Para la estadistica descriptiva
text: El texto del tweet
"""

from pymongo import MongoClient
import csv
import tweepy
import datetime

def calcularCoordenadas(document):
	x0=float(document['place']['bounding_box']['coordinates'][0][2][0])
	x1=float(document['place']['bounding_box']['coordinates'][0][0][0])
	y0=float(document['place']['bounding_box']['coordinates'][0][0][1])
	y1=float(document['place']['bounding_box']['coordinates'][0][1][1])
	return (x1-x0)/2+x0,(y1-y0)/2+y0 #Retorna long,latit

client = MongoClient()
db = client.twitter_db
collection = db.mention_usa_trump.find()

words=['trump','donald trump','realdonaldtrump','trump2016','makeamericagreatagain','hillary','clinton','hillaryclinton','hillary2016','imwither','brexit']

fieldnames = ['id_Tweet','datetime_creation','date_creation', 'time_creation','latitud','longitud','type_location','country_code','country',
			'mention_candidate','screen_name','account_age_year','account_age_month','user_location','lang','source',
			'text_len','text_count_hashtags','text_count_symbols','text_count_urls','text_count_mentions','text']
with open('geolocated.csv', 'wb') as csvfileGeo:
	writerGeo = csv.DictWriter(csvfileGeo, fieldnames=fieldnames)
	writerGeo.writeheader()

	with open('mentions.csv', 'wb') as csvfile:		
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		i=0
		for document in collection:
			if 'retweeted_status' not in document and 'created_at' in document:
				if any(w in document['text'].lower() for w in words):
					date,datetime_creation,date_creation,time_creation,screen_name,account_age,account_age_month,lang= (None,)*8
					lon,lat,type_location,country_code,country= (None,)*5
					text_chash,text_csymbols,text_curls,text_cment,text,mention_candidate= (None,)*6
					location=False
					
					if 'coordinates' in document or 'place' in document:
						if document['coordinates'] != None or document['place'] != None:
							if document['coordinates'] != None:
								if document['coordinates']['type'] == "Point":
									lon=document['coordinates']['coordinates'][0]
									lat=document['coordinates']['coordinates'][1]
									type_location="coordinates"
							elif document['place'] != None:
								lon,lat=calcularCoordenadas(document)
								type_location="place"
								country_code=document['place']['country_code'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' ')
								country=document['place']['country'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' ')
					
					
					date=datetime.datetime.strptime(document['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
					datetime_creation=date.strftime("%d/%m/%Y %H:%M")
					date_creation=date.strftime("%d/%m/%Y")
					time_creation=date.strftime("%H:00")
					screen_name=document['user']['screen_name']

					account_age=datetime.datetime.strptime(document['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
					account_age_year=account_age.strftime("%Y")
					account_age_month=account_age.strftime("%b")

					if document['user']['location'] != None:
						location=True

					text_chash=len(document['entities']['hashtags'])
					text_csymbols=len(document['entities']['symbols'])
					text_curls=len(document['entities']['urls'])
					text_cment=len(document['entities']['user_mentions'])
					
									
					if 'entities' in document:
						user_mentions=document['entities']['user_mentions']
						if any(u['screen_name'] == 'HillaryClinton' for u in user_mentions) or any(u['screen_name'] == 'realDonaldTrump' for u in user_mentions):
							if any(u['screen_name'] == 'HillaryClinton' for u in user_mentions) and any(u['screen_name'] == 'realDonaldTrump' for u in user_mentions):
								mention_candidate='both'
							elif any(u['screen_name'] == 'HillaryClinton' for u in user_mentions):
								mention_candidate='HillaryClinton'
							elif any(u['screen_name'] == 'realDonaldTrump' for u in user_mentions):
								mention_candidate='realDonaldTrump'
							
							writer.writerow({ 'id_Tweet':document['id'],'datetime_creation': datetime_creation,'date_creation': date_creation,
								'time_creation': time_creation,'latitud':lat,'longitud':lon,'type_location':type_location,'country_code':country_code,'country':country,
								'mention_candidate':mention_candidate,'screen_name':screen_name,
								'account_age_year':account_age_year,'account_age_month':account_age_month,
								'user_location':location,
								'lang':document['lang'],
								'source':document['source'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' '),
								'text_len':len(document['text']),'text_count_hashtags':text_chash,'text_count_symbols':text_csymbols,
								'text_count_urls':text_curls,'text_count_mentions':text_cment,
								'text': document['text'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' ')})
							print i
					
					if 'coordinates' in document or 'place' in document:
						if document['coordinates'] != None or document['place'] != None:						
							writerGeo.writerow({ 'id_Tweet':document['id'],'datetime_creation': datetime_creation,'date_creation': date_creation,
									'time_creation': time_creation,'latitud':lat,'longitud':lon,'type_location':type_location,'country_code':country_code,'country':country,
									'mention_candidate':mention_candidate,'screen_name':screen_name,
									'account_age_year':account_age_year,'account_age_month':account_age_month,
									'user_location':location,
									'lang':document['lang'],
									'source':document['source'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' '),
									'text_len':len(document['text']),'text_count_hashtags':text_chash,'text_count_symbols':text_csymbols,
									'text_count_urls':text_curls,'text_count_mentions':text_cment,
									'text': document['text'].encode('utf8').replace('\n',' ').replace('\r',' ').replace('\r\n',' ')})
					
			i=i+1