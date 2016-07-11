import nltk
from nltk.collocations import *
import numpy as np
import pandas as pd

tweets=pd.read_csv("result_text.csv")
text=[]
agregar=lambda x:text.append(str(x))
tweets['text'].apply(agregar)


def get_list_phrases(text,lista_duplas):
	token=nltk.word_tokenize(text)
	c = 0
	while c < len(token) - 2:
		lista_duplas.append((token[c], token[c+1]))
		lista_duplas.append((token[c], token[c+2]))
		c+=1


lista_duplas=[]
lista_source=[]
lista_target=[]
for texto in text:
	get_list_phrases(texto,lista_duplas)

for tupla in  lista_duplas:
	lista_source.append(tupla[0])
	lista_target.append(tupla[1])
df2=pd.DataFrame()
df2['source']=lista_source
df2['target']=lista_target
df2.to_csv('grafo.csv',index=False)
