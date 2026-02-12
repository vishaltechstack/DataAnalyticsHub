'''
scikit-learn basic structure

1. Import model
2. Create object
3. Fit model
4. Predict
5. Evaluate
'''
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[5]])
print("Prediction:", prediction)

'''
Key methods:
    • fit()
    • predict()
    • score()
'''