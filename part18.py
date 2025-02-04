import modin.pandas as pd
df = pd.read_csv('merged.csv')
print(df)
c.groupby('Season').count()

'''
from datetime import time
import requests
import pandas as pd

# url = "https://github.com/krishnaik06/Machine-Learning-in-90-days/blob/master/Section%201-%20Python%20Crash%20Course/Test.csv"
# %%time
c = pd.read_csv("merged.csv")
print(c.head(5))

c.groupby('Season').count()





# =,copy(),deepcopy()

lst = [1,2,3,4,5]
lst2 = lst
print(lst2)
print(lst)
lst2[1] = 100
print(lst2)
print(lst)
print(" ")
#copy() or shallow copy
lst = [1,2,3,4,5]
lst2 = lst.copy()
print(lst2)
lst2[1] = 1000
print(lst2)
print(lst)

lst = [[1,2,3,4],[5,9,6,8,7]]
lst2 = lst.copy()
print(lst," ", lst2)
lst[1][2] = 200
print(lst," ", lst2)
lst.append([3,9,6,5])
print(lst)
print(lst2)
print(" ")

#deepcopy()
import copy
lst = [1,2,3,4,5]
lst2 = lst.deepcopy(lst)
print(lst2)
lst2[1] = 900
print(lst,lst2)


'''
