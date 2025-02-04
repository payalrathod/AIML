# seaborn tutorial
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#a = pd.read_csv('tips.csv')
a = sns.load_dataset('tips')
print(a)

'''
tips = pd.read_csv('tips.csv')
print(tips)

a = sns.load_dataset("tips")
print(a)

data = ('index,col1,col2,col3\n'
        '1,00,11,22\n'
        '2,33,44,55\n'
        '3,66,77,88')
df = sns.load_dataset()
print(df)


df.head()
df.dtypes()
df.corr()
sns.heatmap(df.corr())
sns.jointplot(x='tip',y='totalbill',data=df,kind='hex')
sns.jointplot(x='tip',y='totalbill',data=df,kind='reg')
df['somker'].value_counts()
sns.pairplot(df, hue='tip')
sns.displot(df['tip'])
#plt.show(sns)


sns.countplot('age', data=df)
sns.barplot(x='totalbill',y='smoker', data=df)
sns.boxplot('smoker','totalbill',hue='smoker',data=df,palette='rainbow')
sns.jointplot()
'''

matplotlib.pyplot.show()