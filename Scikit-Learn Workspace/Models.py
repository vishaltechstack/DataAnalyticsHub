# Training different ML models


from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X, y)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, y)

print("Models trained successfully")