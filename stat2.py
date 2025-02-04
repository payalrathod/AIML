import pandas as pd

df = pd.read_csv("wine.csv",header=None, usecols=[0,1,2])
print(df.head())
df.columns = ['Class', 'Alcohol', 'Malic']
print(df.head())

from sklearn.preprocessing import MinMaxScaler, StandardScaler

# scaling = MinMaxScaler()
# print(scaling.fit_transform(df[['Alcohol','Malic']]))

# standardization
scaling = StandardScaler()
print(scaling.fit_transform(df[['Alcohol', 'Malic']]))







