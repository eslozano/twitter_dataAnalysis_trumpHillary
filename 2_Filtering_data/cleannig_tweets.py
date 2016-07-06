import numpy as np
import pandas as pd
import re,string
import nltk
from nltk.corpus import stopwords


def delete_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def delete_hashtag_target(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word=='@HillaryClinton':
                word='HillaryClinton'
            if word=='@realDonaldTrump':
                word= 'realDonaldTrump'
            if Is_stopwords(word)=='true':
                word='@'
            if  word[0] not in entity_prefixes or word=='#Hillary'or word=='Clinton'or word=='HillaryClinton'or word=='Hillary2016'or word=='ImWither' or word=='trump'or word=='Donald Trump'or word=='realDonaldTrump'or word=='trump2016'or word=='MakeAmericaGreatAgain':
                words.append(word)
    return ' '.join(words)


tests = [
    "@peter  the the of of by @HillaryClinton the , I really, love that: shirt; at #Macy. https://bet.ly//WjdiW4",
    "@shawn  @realDonaldTrump Titanic tragedy could have been prevented Economic Times: Telegraph.co.ukTitanic tragedy could have been preve... http://bet.ly/tuN2wx",
    "I am at Starbucks http://4sh.com/samqUI (7419 3rd ave, at 75th, Brooklyn)",
]

def Is_stopwords(word):
    if word in stopwords.words('english'):
        return 'true'
    else:
        return 'false'

        

#for t in tests:
#    print delete_hashtag_target(delete_links(t))



tweets=pd.read_csv("statistics.csv")
print tweets.head()
text=[]
agregar=lambda x:text.append(str(x))
tweets['text'].apply(agregar)
print text[0]
nuevo_texto=[]
for t in text:
    nuevo_texto.append(delete_hashtag_target(delete_links(t)))
#data={'text':nuevo_texto}
df2=tweets.copy()
df2=df2.drop('text',1)
df2['text']=nuevo_texto
print df2.head()
df2.to_csv('tweets_limpios.csv')

