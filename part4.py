from typing import List

import pandas as pd
from pandas import DataFrame


df = '{"employee_name": "James", "email": "json@gmail.com", "job_profile": [{"title1": "Manager", "title2": "Associate"}]}'
df1 = pd.read_json(df)
df1 = df1.to_json(orient="records")
print(df1)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
print(df.head())
df.to_csv('wine.csv')

#reading html content
#url = 'https://en.wikipedia.org/wiki/Mobile_country_code'
#df2 = pd.read_html(url)
#print(type(df2))
#print(df2[0])
#df2 = pd.read_html(url, match='Country', header=0)
#print(df2[0])

#df = pd.read_excel('POA - Tracker (1).xlsx')
#df = df.head()
#print(df)
#df.to_pickle('df')
#df = pd.read_pickle('df')
#df.head()



