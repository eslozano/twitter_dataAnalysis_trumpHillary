import pandas as pd

df1 = pd.read_csv('dataset_mentions.csv',sep=',',error_bad_lines=False,na_values=[''])
df2=df1[df1.type_location.notnull()]
df2.to_csv('dataset_mention_geolocated.csv',index=False)