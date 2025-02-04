# list are iterable allocated in memory location
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pyforest
from pyforest import active_imports, sns

lst = [1, 2, 3, 4, 5, 6, 7]
for i in lst:
    print(i)
print("..")
lst1 = iter(lst)
print(lst1)
print(next(lst1))
print("..")
for i in lst1:
    print(i)

df = pd.read_csv('tips.csv')
print(df.head())

active_imports()

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 4, 2, 6, 8]

plt.plot(lst1, lst2)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

active_imports()

print(np.array([1, 2, 3, 4, 5]))

df1 = pd.read_csv('wine.csv')
print(df1.head())

#sns.distplot({'y'})

active_imports()
