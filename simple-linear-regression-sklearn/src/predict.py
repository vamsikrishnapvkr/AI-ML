import pandas as pd
import joblib
from src.config import MODEL_PATH, FEATURE

def load_model():
    return joblib.load(MODEL_PATH)


def predict(hours):
    model = load_model()

    X = pd.DataFrame([[hours]], columns=[FEATURE])
    return model.predict(X)[0]


def batch_predict(values):
    model = load_model()

    X = pd.DataFrame(values, columns=[FEATURE])
    return model.predict(X)