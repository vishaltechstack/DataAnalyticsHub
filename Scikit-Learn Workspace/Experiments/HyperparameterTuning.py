# Nested GridSearch with pipeline

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from src.preprocessing import create_preprocessor

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 10]
}

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="f1"
)

grid.fit(X_train, y_train)
print(grid.best_params_)