# End-to-end training pipeline

import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from config.config import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE, MODEL_NAME
from src.data_loader import load_data
from src.preprocessing import create_preprocessor
from src.feature_engineering import add_features
from src.model_factory import get_model

df = load_data()
df = add_features(df)

X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

num_features = X.select_dtypes(include=["int64", "float64"]).columns
cat_features = X.select_dtypes(include=["object"]).columns

preprocessor = create_preprocessor(num_features, cat_features)
model = get_model(MODEL_NAME)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
)

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "models/trained_model.pkl")
print("Model trained and saved")
