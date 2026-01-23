# Scaler + Model together (very important)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y)

pipeline.fit(X_train, y_train)
print("Pipeline accuracy:", pipeline.score(X_test, y_test))