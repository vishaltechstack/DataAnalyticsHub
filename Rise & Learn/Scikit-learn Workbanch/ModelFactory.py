from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def get_model(model_name):

    if model_name == "logistic":
        return LogisticRegression(max_iter=1000)

    if model_name == "svm":
        return SVC(probability=True)

    if model_name == "random_forest":
        return RandomForestClassifier(n_estimators=200)

    raise ValueError("Invalid model name")