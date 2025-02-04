import numpy as np
import pandas as pd

a = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'],
                 columns=['column1', 'column2', 'column3', 'column4'])
# print(a.head())
# a.to_csv('Test1.csv')
# print(type(a.loc['Row1']))
# print(a.loc['Row1'])
# print(a.iloc[0:3,0:2])
# print(a.iloc[:, 1:].values)
# print(a.iloc[:, 1:].value_counts())
# print(a.isnull().sum())
# print(a['column1'].value_counts())
# print(a['column1'].unique())
print(a[['column2', 'column3']])
