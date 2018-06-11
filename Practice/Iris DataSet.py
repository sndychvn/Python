import pandas as pd
import numpy as np
import sklearn as sk
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
print(iris)
print(iris.data)
print(iris.keys())
print(iris.target)
print(iris.target_names)
print(iris.DESCR)
print(iris.data.shape)
print(iris.data.dtype)
pd_X = pd({iris.feature_names[0]: iris.data[:, 0]})
print(pd_X.iloc[:10, :])
