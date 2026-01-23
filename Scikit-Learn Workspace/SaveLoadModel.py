# Save and load trained model

import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

model = LinearRegression()
model.fit(X, y)

# Save
joblib.dump(model, "linear_model.pkl")

# Load
loaded_model = joblib.load("linear_model.pkl")
print(loaded_model.predict([[4]]))