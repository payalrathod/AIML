import numpy as np
from numpy import array

lst = [1, 2, 3, 4, 5]
arr = array(lst)
# print(type(arr))
# print(arr)
# print(arr.shape)

lst1 = [1, 2, 3, 4, 5]
lst2 = [9, 8, 7, 6, 5]
arr2 = np.array([lst1, lst2])
# print(arr2[:, :])
# print(arr2[0:, 3:])
# print(arr2[1:, 1:4])
# print(arr2)
# print(arr2.shape)
# print(arr2.reshape(5, 2))
# print(arr2.reshape(1, 10))

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr3[3])
#arr3 = np.arange(0, 10, step=2)
# print(arr3)
# print(np.linspace(1,10,20))
#arr3[3:] = 100  #copy and broadcasting
#arr3 = lst.copy()
#print(arr3<5)

#arr3 = np.ones(4)
#arr3 = np.ones(4,dtype=int)
#arr3 = np.ones((2,5), dtype=float)
print(arr3)

#arr3 = np.random.rand(3,3)
#print(arr3)
#arr3 = np.random.randn(4,4)
#print(arr3)
arr3 = np.random.randint(0,100,8).reshape(2,4)
print(arr3)









