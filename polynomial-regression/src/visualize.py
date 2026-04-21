import pandas as pd
import matplotlib.pyplot as plt
import joblib

def visualize():
    df = pd.read_csv("data/processed/clean.csv")

    X = df.drop("SalePrice", axis=1)
    y = df["SalePrice"]

    model = joblib.load("models/model.pkl")

    y_pred = model.predict(X)

    plt.scatter(y, y_pred, alpha=0.5)
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted (Polynomial Regression)")
    plt.show()

if __name__ == "__main__":
    visualize()