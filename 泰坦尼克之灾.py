# -*-coding:utf-8 -*-

"""
# File       : 泰坦尼克之灾.py
# Time       ：2020/6/30 下午4:12
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""

import pandas as pd
import random
import statsmodels.formula.api as smf
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt


def add_random(x):
    return x # + random.random() / 3


data_train = pd.read_csv('data/titanic-data-train.csv')
panel = pd.DataFrame(index=data_train.index)
panel['Class'] = data_train['Pclass'].apply(lambda x: add_random(x))
panel['Age'] = data_train['Age'].apply(lambda x: add_random(x))
panel['Sex'] = data_train['Sex']
panel.replace('male', 0, inplace=True)
panel.replace('female', 1, inplace=True)
panel['Sex'] = panel['Sex'].apply(lambda x: add_random(x))
panel['Parch'] = data_train['Parch'].apply(lambda x: add_random(x))
panel['Survived'] = data_train['Survived'].apply(lambda x: add_random(x))
panel = panel.dropna()
print(panel.head())

sm = scatter_matrix(panel, figsize=(12, 7))
# plt.show()

corr_array = panel.corr()['Survived']
print(corr_array)

formula = 'Survived~Sex+Class'
lm = smf.ols(formula=formula, data=panel).fit()
print(lm.summary())

