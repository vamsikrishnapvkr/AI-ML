import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from src.config import DATA_PATH, MODEL_PATH, FEATURE, TARGET
from src.model import get_model


def train_model():
    df = pd.read_csv(DATA_PATH)

    X = df[[FEATURE]]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = get_model()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("\n Evaluation Metrics")
    print("MSE:", mean_squared_error(y_test, preds))
    print("R2 :", r2_score(y_test, preds))

    joblib.dump(model, MODEL_PATH)
    print("\n Model saved at", MODEL_PATH)

    return model