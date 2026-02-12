# Advanced evaluation metrics

from sklearn.metrics import classification_report, roc_auc_score
import joblib
from src.data_loader import load_data
from config.config import TARGET_COLUMN

model = joblib.load("models/trained_model.pkl")
df = load_data()

X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

y_pred = model.predict(X)
y_prob = model.predict_proba(X)[:, 1]

print(classification_report(y, y_pred))
print("ROC AUC:", roc_auc_score(y, y_prob))