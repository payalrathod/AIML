from io import StringIO

import matplotlib_inline
import numpy as np
import pandas as pd
import urllib
import pyforest
# from pyforest import active_imports, pd, plt, np, sns
from matplotlib import pyplot as plt

lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
# print(arr)
# print(type(arr))
# print(arr.shape)
lst2 = [6, 7, 8, 9, 10]
lst3 = [12, 13, 45, 54, 76]
arr1 = np.array([lst, lst2, lst3])
# print(arr1)
# print(arr1.shape)
# print(arr1.reshape(1,15))
# print(arr1.shape)
# print(arr[3])
# print(arr1[1:4,2:4])

arr2 = np.arange(0, 10, step=2)
# print(arr2)
arr3 = np.linspace(1, 10, 50)
# print(arr3)

# arr[2:] = 100
# print(arr)  # copy fn and broadcasting
# arr = arr1
# arr1[1:] = 500
# print(arr1)
# print("  ")
# print(arr)


arr1 = arr.copy()
arr1[2:] = 900
# print(arr1)
# print(arr)

val = 2
# print(arr < 2)
# print(arr * 3)
# print(arr[arr < 3])
#
# print(np.ones(4, dtype=int))
# print(np.ones((2, 4), dtype=float))
#
# print(np.random.rand(2, 4))
# print(" ")
# print(np.random.randn(3, 4))

# arr_ex = np.random.randn(4, 4)
# print(arr_ex)
# import seaborn as sns
# sns.distplot(pd.DataFrame(arr_ex.reshape(16,1)))
# print(np.random.randint(0,100,8).reshape(4,2))
# print(np.random.random_sample(1,5))


# Pandas
df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['r1', 'r2', 'r3', 'r4', 'r5'],
                  columns=['c1', 'c2', 'c3', 'c4'])
# print(df.head())
# print(df.to_csv('a.csv'))
# print(df.loc['r1'])
# print(type(df.loc['r1']))
# print(df.iloc[0:2,2:4])
# print(type(df.iloc[0:2,2:4]))
# print(df.iloc[0:2,2:4].values)
# print(df.values.shape)
# print(df)
# print(df.isnull().sum())
# print(df['c1'].value_counts())
# print(df['c1'].unique())
# print(df[['c1','c4']])

# Pandas Part 2
df = pd.read_csv('wine.csv')
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df['1'].value_counts())
# print(df[df['2']>10])
# print(" ")

from io import StringIO, BytesIO

data = ('col1, col2, col3\n'
        'x,y,z\n'
        'a,b,2\n'
        'c,d,3')
# print(type(data))
# print(StringIO)
# print(pd.read_csv(StringIO(data)))
df1 = pd.read_csv(StringIO(data), usecols=['col1'])
# print(df1)
# df1.to_csv('abc.csv')

df2 = pd.read_csv(StringIO(data), dtype=object)
# print(df2)
# print(df2['col1'][2])
# print(df2['col1'])

# df2 = pd.read_csv(StringIO(data), dtype={'b': int,'c':float,'a': 'Int64'})
# print(df2.dtypes)

data2 = ('index,a,b,c\n'
         '4,apple,bat,5.7\n'
         '8,orange,cow,10')
# print(pd.read_csv(StringIO(data2), index_col=0))
# print(pd.read_csv(StringIO(data2)))
# print(pd.read_csv(StringIO(data2), index_col=2))
# print(pd.read_csv(StringIO(data2), index_col=False))
# print(pd.read_csv(StringIO(data2), usecols=['b','c'], index_col=False))

# Part 3
data3 = '[{"name":"abc", "mail":"abc@mail.com","phone":"3453"}]'
# print(pd.read_json(data3))

df3 = pd.read_csv('wine.csv')
# print(df3.head())
# print(df3.to_json(orient="index")) #obj to jsom
# print(df3.to_json(orient="records"))

# url = 'https://en.wikipedia.org/wiki/Main_Page'
# df4 = pd.read_html(url)
# print(type(df4))
# print(df4[0])

df_excel = pd.read_excel('abcde.xlsx')
# print(df_excel)
df_excel.to_pickle('df_excel')
df4 = pd.read_pickle('df_excel')
# print(df4)

# matplotlib
# import matplotlib.pyplot as plt

# matplotlib_inline
x = np.arange(0, 10)
y = np.arange(11, 21)
a = np.arange(40, 50)
b = np.arange(50, 60)


# scatter plot
# plt.scatter(x,y,c='g')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('graph')
# plt.savefig('test.jpeg')
# plt.plot(x,y,'r*--')
# plt.show()


# import seaborn as sns
# df5 = sns.load_dataset('tips')
# print(df5.head())


# Functions
def evenodd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


def summ(n1, n2):
    return (n1 + n2)


# print(evenodd(23))
# a = evenodd(22)
# print(a)

# print(summ(2, 5))


def hello(name, age=20):
    return ("name {}, age {}".format(name, age))


# print(hello('jka'))
# positional and keyword arguments

def hel1(*args, **kwargs):
    print(args)
    print(kwargs)


# print(hel1("abc","def",age=23,dob=1990))

lst = ['ahs', 'jshd']
dictor = {'age': 23, 'dob': 1990}
# hel1(*lst,**dictor)

lm = [1, 2, 3, 4, 5, 6, 7]


def evenoddsum(lm):
    ec = 0
    oc = 0
    for i in lm:
        if i % 2 == 0:
            ec = ec + i
        else:
            oc = oc + i
    return "even:", ec, "odd:", oc


# print(evenoddsum(lm))


# Map function

def even_odd(numb):
    if numb % 2 == 0:
        return ("even: ", numb)
    else:
        return ("odd: ", numb)


# print(even_odd(21))

lst6 = [1, 32, 54, 67, 30, 98, 2, 92]
# print(map(even_odd,lst6))
# print(list(map(even_odd,lst6)))

# Lambda function
a = lambda n1, n2: n1 + n2
# print(a(1,3))

b = lambda n: n % 2 == 0


# print(b(4))


# Filter function
def eve_odd(numb):
    if numb % 2 == 0:
        return True


lm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(list(filter(eve_odd,lm)))
# print(list(filter(lambda n1: n1%2 == 0, lm)))
# print(list(map(filter(lambda n1: n1%2 == 0, lm))))

# List Comprehension
lv = []


def lst_sq(lst7):
    for i in lst7:
        lv.append(i * i)
    return lv


# print(lst_sq([2,3,4,5,6]))

ls = [2, 3, 4, 5, 6, 7, 8]
a = [i * i for i in ls if i % 2 == 0]


# print(a)

# String formatting
def greeti(name):
    return "hello {}".format(name)


# print(greeti('lam'))

def wel(fn, ln):
    return "welcome {ln} {fn}".format(fn=fn, ln=ln)


# print(wel('eds','thr'))

# list iterables vs iterators
lh = [1, 2, 3, 4, 5, 6, 7]
# for i in lh:
#     print(i)

ab = iter(lh)
# print(next(ab))
# print(next(ab))
# for i in lh:
#     print(i)

df = pd.read_csv('wine.csv')
# print(df.head())
# print(active_imports())
lh = [1, 2, 3, 4, 5, 6, 7]
ls = [2, 3, 4, 5, 6, 7, 8]

plt.plot(lh, ls)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# print(np.array([2,5,3,2,7,8,0]))
df2 = pd.read_csv('tips.csv')


# print(df2.head())
# sns.distplot(df2)
# print(active_imports())


# OOPS
# class Car:
#     pass
#
# car1 = Car()
# print(car1)
# car1.windows = 5
# car1.doors = 4
# print(car1.windows)
# car2 = Car()
# car2.windows = 2
# car2.doors = 2
# print(car2.doors)
# car2.engine = 'petrol'
# print(car2.engine)
#
# print(dir(car1))
# class Car:
#     def __init__(self, window, door, enginetype):
#         self.window = window
#         self.door = door
#         self.enginetype = enginetype
#
#     def selfdrive(self):
#         # self.drive = drive
#         return "self driving {} car".format(self.enginetype)
#
#
# car1 = Car(3, 4, 'petrol')


# print(car1)
# print(car1.window, car1.door, car1.enginetype)
# print(car1.selfdrive())


# exception handling
# try:
# a = n
# n = 's'
# a = 1
# n = a + n
# a = int(input())
# b = int(input())
# c = a/b
# d = a*b
# e = a+b
# print(c)
# print(d)
# print(e)
# except NameError as nm:
#     print('user didnt define variable')
# except ZeroDivisionError as ze:
#     print('provide number greater than 0')
# except TypeError as te:
#     print('different data type')
# except Exception as ex:
#     print(ex)
# else:
# print(c)
# print(d)
# print(e)

# try:
#     a = int(input('n1: '))
#     b = int(input('n2: '))
#     c = a/b
# except NameError as nm:
#     print('user didnt define variable')
# except ZeroDivisionError as ze:
#     print('provide number greater than 0')
# except TypeError as te:
#     print('different data type')
# except Exception as ex:
#     print(ex)
# else:
#     print(c)
# finally:
#     print('done execution')


# custom exception
# class Error(Exception):
#     pass
# class DOB(Error):
#     pass
#
# year = int(input('DOB: '))
# age = 2022-year
# try:
#     if 30 >= age > 20:
#         print('valid age')
#     else:
#         raise DOB
# except DOB:
#     print('invalid age')


# public _protected and __private access modifiers
class Car189():
    def __init__(self, win, door, engine):
        self.__win = win
        self.__door = door
        self.__engine = engine


a = Car189(2, 2, 'petrol')
# print(a)
# print(dir(a))
b = Car189(4, 2, 'diesel')


# print(dir(b))

class truck(Car189):  # protected variable
    def __init__(self, win, door, engine, power):
        super().__init__(win, door, engine)
        self.power = power


truc = truck(4, 4, 'deisel', 4000)


# print(dir(truc))


# oops inheritance
class Car19():
    def __init__(self, win, door, engine):
        self.win = win
        self.door = door
        self.engine = engine

    def drive(self):
        print('person drive car')


c1 = Car19(3, 4, 'petrol')
# print(c1.win)
# print(dir(Car19))
# print(c1.drive())

# import logging


class audi(Car19):
    def __init__(self, win, door, engine, ai):
        super().__init__(win, door, engine)
        self.ai = ai

    def selfdrive(self):
        print('self driving car')


c2 = audi(3, 3, 'petrol', 'music')
# print(c2.selfdrive())
# print(dir(c2))
# print(c2.ai)


















