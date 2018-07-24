import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)






iris = datasets.load_iris()
X = iris.data[:, :]
Y = iris.target
h = .02
print(logreg)
