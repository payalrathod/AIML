import pandas as pd
from io import StringIO, BytesIO

a = pd.read_csv('Test1.csv')
# print(a.head())
# print(a.info())
# print(a.describe())
# print(a['column1'].value_counts())
# print(a[a['column1'] < 6])

data = ('index,col1,col2,col3\n'
        '1,00,11,22\n'
        '2,33,44,55\n'
        '3,66,77,88')
# print(type(data))
# print(pd.read_csv(StringIO(data)))
# print(pd.read_csv(StringIO(data), usecols=['col1', 'col3']))
# aa = pd.read_csv(StringIO(data), dtype=float)   #dtype=int,object,float
# print(aa)
# print(aa['col1'])

'''aa = pd.read_csv(StringIO(data), dtype={'col2': int, 'col3':float, 'col1': 'Int64'})
print(aa)
print(type(aa['col1'][1]))
print(aa.dtypes) 

aa = pd.read_csv(StringIO(data), index_col=2)
print(aa)  # remove col2 to understand

aa1 = pd.read_csv(StringIO(data), index_col=False)
print(aa1)

aa2 = pd.read_csv(StringIO(data), usecols=['col1', 'col3'], index_col=False)
print(aa2)
'''

dataa = 'a,b\n"hello, \\"My name\\", age", 35'
dataa = pd.read_csv(StringIO(dataa), escapechar="\\")
print(dataa)

df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep= '\t')
print(df.head())
