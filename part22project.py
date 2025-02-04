# feature engineering
import matplotlib_inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matplotlib_inline
pd.pandas.set_option('display.max_columns', None)

dataset = pd.read_csv('train.csv')
print(dataset.head())

# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(dataset,dataset['SalePrice'],test_size=0.1,random_state=0)
# print(x_train.shape)
# print(x_test.shape)

features_nan = [feature for feature in dataset.columns if
                dataset[feature].isnull().sum() > 1 and dataset[feature].dtypes == 'O']
for feature in features_nan:
    print("{}: {}% missing values".format(feature, np.round(dataset[feature].isnull().mean(), 4)))


# replace nan values with word missing
def replace_cat_feature(dataset, features_nan):
    data = dataset.copy()
    data[features_nan] = data[features_nan].fillna('Missing')
    return data


dataset = replace_cat_feature(dataset, features_nan)
print(dataset[features_nan].isnull().sum())
print(dataset.head())

numerical_with_nan = [feature for feature in dataset.columns if
                      dataset[feature].isnull().sum() > 1 and dataset[feature].dtypes != 'O']
for feature in numerical_with_nan:
    print("{}: {}% missing values".format(feature, np.around(dataset[feature].isnull().mean(), 4)))

for feature in numerical_with_nan:
    median_value = dataset[feature].median()
    dataset[feature + 'nan'] = np.where(dataset[feature].isnull(), 1, 0)
    dataset[feature].fillna(median_value, inplace=True)
print(dataset[numerical_with_nan].isnull().sum())
print(dataset.head())

# temporal variables
for feature in ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt']:
    dataset[feature] = dataset['YrSold'] - dataset[feature]
print(dataset.head())

# log normal distribution
num_features = ['LotFrontage', 'LotArea', '1stFlrSF', 'GrLivArea', 'SalePrice']
for feature in num_features:
    dataset[feature] = np.log(dataset[feature])
print(dataset.head())

# rare categorial feature
categorial_features = [feature for feature in dataset.columns if dataset[feature].dtype == 'O']
print(categorial_features)
for feature in categorial_features:
    temp = dataset.groupby(feature)['SalePrice'].count() / len(dataset)
    temp_df = temp[temp > 0.01].index
    dataset[feature] = np.where(dataset[feature].isin(temp_df), dataset[feature], 'Rare_var')
print(dataset.head())

# not working
# Feature Scaling
'''
feature_scale = [feature for feature in dataset.columns if feature not in ['Id', 'SalePrice']]

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(dataset[feature_scale])

data = pd.concat([dataset[['Id', 'SalePrice']].reset_index(drop=True),pd.DataFrame(scaler.transform(dataset[feature_scale]), columns=feature_scale)],axis=1)
print(data.head())

data.to_csv('x_train.csv', index=False)

# Part 2 of feature scaling
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel

dataset = pd.read_csv('x_train.csv', None)
dataset.head()
y_train = dataset[['SalePrice']]
x_train = dataset.drop(['Id', 'SalePrice'],axis=1)
feature_sel_model = SelectFromModel(Lasso(alpha=0.005, random_state=0))
feature_sel_model.fit(x_train, y_train)
print(feature_sel_model.get_support())

selected_feat = x_train.columns[(feature_sel_model.get_support())]
print('total features: {}'.format((x_train.shape[1])))
print('selected features: {}'.format(len(selected_feat)))
print('features with coefficients shrank to zero: {}'.format(np.sum(sel_.estimator_.coef_ == 0)))
print(selected_feat)
x_train = x_train[selected_feat]
x_train.head()
'''
