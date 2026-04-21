import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score

def evaluate():
    df = pd.read_csv("data/processed/clean.csv")

    X = df.drop("SalePrice", axis=1)
    y = df["SalePrice"]

    model = joblib.load("models/model.pkl")

    y_pred = model.predict(X)

    print("MSE:", mean_squared_error(y, y_pred))
    print("R2 Score:", r2_score(y, y_pred))

if __name__ == "__main__":
    evaluate()