# Scaling, missing values, encoding

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

X = np.array([[1, 2], [3, np.nan], [7, 6]])

# Handle missing values
imputer = SimpleImputer(strategy="mean")
X_imputed = imputer.fit_transform(X)

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

print(X_scaled)


'''
Other tools:
• MinMaxScaler
• RobustScaler
• LabelEncoder
• OneHotEncoder
'''

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def create_preprocessor(num_features, cat_features):

    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_features),
        ("cat", cat_pipeline, cat_features)
    ])

    return preprocessor