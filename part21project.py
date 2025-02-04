# exploratory data analysis

from typing import Union, Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader
pd.pandas.set_option('display.max_columns', None)
dataset = pd.read_csv('train.csv')

print(dataset.shape)
print(dataset.head())

fea_na = [fea_na for fea_na in dataset.columns if dataset[fea_na].isnull().sum()>1]
for feat in fea_na:
    print(feat, np.round(dataset[feat].isnull().mean(), 4), '% missing values')

# for feat in fea_na:
#     data = dataset.copy()
#     data[feat] = np.where(data[feat].isnull(), 1, 0)
#     data.groupby(feat)['SalePrice'].median().plot.bar()
#     plt.title(feat)
#     plt.show()

print("ID of houses: {}".format(len(dataset.Id)))

num_feat = [feat for feat in dataset.columns if dataset[feat].dtypes != 'O'] #list comphrehension

print('No. of numerical variable: ', len(num_feat))
dataset[num_feat].head()

year_feat = [feat for feat in num_feat if 'Yr' in feat or 'Year' in feat]
print(year_feat)

for feat in year_feat:
    print(feat, dataset[feat].unique())

# dataset.groupby('YrSold')['SalePrice'].median().plot()
# plt.xlabel('Year Sold')
# plt.ylabel('Median House Price')
# plt.title('House Price vs YearSold')
# plt.show()

print(year_feat)

# for feat in year_feat:
#     if feat != 'YrSold':
#         data = dataset.copy()
#         data = data['YrSold']-data[feat]
#         plt.scatter(data[feat], data['SalePrice'])
#         plt.xlabel(feat)
#         plt.ylabel('SalePrice')
#         plt.show()

discrete_feature = [feat for feat in num_feat if len(dataset[feat].unique())<25 and feat not in year_feat+['Id']]
print("discrete variable count: {}".format(len(discrete_feature)))
print(discrete_feature)
print(dataset[discrete_feature].head())

for feat in discrete_feature:
    data = dataset.copy()
    data.groupby(feat)['SalePrice'].median().plot.bar()
    plt.xlabel(feat)
    # plt.ylabel('SalesPrice')
    # plt.title(feat)
    # plt.show()

# continuous variable
continuous_feature = [feat for feat in num_feat if feat not in discrete_feature + year_feat+['Id']]
print("Continuous feature: {}".format(len(continuous_feature)))

for feat in continuous_feature:
    data = dataset.copy()
    data[feat].hist(bins=25)
    # plt.xlabel(feat)
    # plt.ylabel("Count")
    # plt.show()



# logarithmic transformation


for feature in continuous_feature:
    data = dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature] = np.log(data[feature])
        data['SalePrice'] = np.log(data['SalePrice'])
        plt.scatter(data[feature],data['SalePrice'])
        # plt.xlabel('feature')
        # plt.ylabel('SalesPrice')
        # plt.title(feature)
        # plt.show()


# Outliers
for feature in continuous_feature:
    data = dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature] = np.log(data[feature])
        data.boxplot(column=feature)
        # plt.ylabel(feature)
        # plt.title(feature)
        # plt.show()

# Categorial variables
categorial_feature = [feature for feature in dataset.columns if data[feature].dtypes == 'O']
print(categorial_feature)

print(dataset[categorial_feature].head())

for feature in categorial_feature:
    print("the feature is {} and number of categories are {}".format(feature,len(dataset[feature].unique())))


for feature in categorial_feature:
    data = dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()














