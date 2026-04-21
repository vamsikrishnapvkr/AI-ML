import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
import joblib
import os

def train():
    df = pd.read_csv("data/processed/clean.csv")

    X = df.drop("SalePrice", axis=1)
    y = df["SalePrice"]

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("poly", PolynomialFeatures(degree=2)),
        ("lr", LinearRegression())
    ])

    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

    print("Model trained and saved!")

if __name__ == "__main__":
    train()