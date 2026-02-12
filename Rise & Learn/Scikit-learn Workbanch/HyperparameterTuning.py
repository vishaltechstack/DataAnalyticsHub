# GridSearchCV

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

params = {
    "n_estimators": [50, 100],
    "max_depth": [None, 5, 10]
}

model = RandomForestClassifier()
grid = GridSearchCV(model, params, cv=5)

grid.fit(X, y)

print("Best Parameters:", grid.best_params_)