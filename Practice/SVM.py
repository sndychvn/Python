import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets

digits = datasets.load_digits()

print(digits)
print(digits.data)
print(digits.target)
print(digits.images[0])

clf = svm.SVC(gamma=0.001, C=100)
x,y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)
print(x,y)
print('Predict:',clf.predict(digits.data[-4:1795]))
plt.imshow(digits.images[-4], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
