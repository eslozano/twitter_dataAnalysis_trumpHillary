#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
El presente script es para remover los tweets que de pronto se encuentran en ambos datasets,
ya que se uso el mismo bounding box para recolectar ambos datasets, también sirve para unir los 
datasets de dos semanas distintas
"""
import pandas as pd
import numpy as np
from datetime import datetime,time,date

df1 = pd.read_csv('dataset_mentionTrump.csv',sep=',',error_bad_lines=False,na_values=[''])

df2 = pd.read_csv('dataset_mentionHillary.csv',sep=',',error_bad_lines=False,na_values=[''])

frames = [df1, df2]
result = pd.concat(frames)

final = result.drop_duplicates(['id_Tweet'])
final.to_csv('dataset_mentions.csv',index=False)

print len(df1.index)
print len(df2.index)
print len(result.index)