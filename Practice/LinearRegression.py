import sklearn as sk
import pandas as pd
from pandas import DataFrame
from sklearn import datasets

iris = datasets.load_iris()
#print(iris)
#print(iris.data)
#print(iris.data.shape)
#print(iris.data.dtype)
print(iris.feature_names[0:10])
print(iris.data[0:10])
pd_X = DataFrame.from_dict({iris.feature_names[0]: iris.data[ : , 0]}, orient = 'index')
print(iris.feature_names[1])
print(iris.data[1])

pd_X = DataFrame({iris.feature_names[0]: iris.data[ : , 0]})
print(pd_X.iloc[:10, :])
Df_pd = DataFrame(iris.data, columns=iris.feature_names)
print(Df_pd.iloc[:10, :])