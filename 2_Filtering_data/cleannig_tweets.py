#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import numpy as np
import pandas as pd
import re,string
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
#nltk.download()
def delete_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return 0

def stemmer_word(text):
    text1 = nltk.word_tokenize(text)
    lmtzr = WordNetLemmatizer()
    tagged = nltk.pos_tag(text1)
    for element in tagged:
        if get_wordnet_pos(element[1])!= 0:
            text = text.replace(element[0],lmtzr.lemmatize(element[0],get_wordnet_pos(element[1])))
        else:
            text = text.replace(element[0],lmtzr.lemmatize(element[0]))
    return text
    
def no_emoticons(text):
    for word in text.split():
        word = word.strip()
        if not((re.search('^[a-z]',word)) or (word=='#hillary'or word=='#clinton'or word=='#hillaryclinton'or word=='#hillary2016'or word=='#imwithher' or word=='#trump'or word=='#donald trump'or word=='#realdonaldtrump'or word=='#trump2016'or word=='#makeamericagreatagain')):
            text = text.replace(word,'')
    return text
    
def delete_hashtag_target(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word and len(word)>3:
            if word=='#hillary'or word=='#clinton'or word=='#hillaryclinton'or word=='#hillary2016'or word=='#imwithher' or word=='#trump'or word=='#donald trump'or word=='#realdonaldtrump'or word=='#trump2016'or word=='#makeamericagreatagain':
                words.append(word)
            if word=='@hillaryclinton':
                word='hillaryclinton'
            if word=='@realdonaldtrump':
                word= 'realdonaldtrump'
            if Is_stopwords(word)=='true':
                word='@'
            if not (word.isalnum()):
                word ='@'
            if word[0] not in entity_prefixes :
                words.append(word)
    return ' '.join(words)

tests = [
    "@peter the the of #hillary he‚ô•Ô∏èflg/more than hisüíÉaye running hugging of by  @hillaryclinton the , i really, love :d :c :/ that: shirt; at #macy. https://bet.ly//WjdiW4",
    "@shawn  @realdonaldtrump titanic tragedy could have been prevented economic times: telegraph.co.ukTitanic tragedy could have been preve... http://bet.ly/tuN2wx",
    "i am at  #imwithher starbucks http://4sh.com/samqUI (7419 3rd ave, at 75th, brooklyn)",
]

def Is_stopwords(word):
    if word in stopwords.words('english'):
        return 'true'
    else:
        return 'false'

        

#for t in tests:
#    print  stemmer_word(no_emoticons(delete_hashtag_target(delete_links(t))))


tweets=pd.read_csv("statistics.csv")
serie1=tweets['text'].str.lower()
tweets=tweets.drop('text',1)
tweets['text']=serie1

text=[]
agregar=lambda x:text.append(str(x))
tweets['text'].apply(agregar)

nuevo_texto=[]
for t in text:
    nuevo_texto.append(stemmer_word(no_emoticons(delete_hashtag_target(delete_links(t)))))

data={'text':nuevo_texto}
df2=tweets.copy()
df2=df2.drop('text',1)
df2['text']=nuevo_texto
#print df2.head()

df2.to_csv('tweets_limpios.csv')
