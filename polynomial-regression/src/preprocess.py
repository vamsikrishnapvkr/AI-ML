import pandas as pd
import os

def preprocess():
    df = pd.read_csv("data/raw/train.csv")

    # Select only numeric features for polynomial regression
    df = df.select_dtypes(include=['int64', 'float64'])

    # Handle missing values
    df = df.fillna(df.mean())

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/clean.csv", index=False)

    print("Preprocessing complete!")

if __name__ == "__main__":
    preprocess()