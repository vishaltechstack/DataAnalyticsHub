# Cross-validation done right

from sklearn.model_selection import cross_val_score
import joblib

model = joblib.load("models/trained_model.pkl")

scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print("Mean F1 Score:", scores.mean())