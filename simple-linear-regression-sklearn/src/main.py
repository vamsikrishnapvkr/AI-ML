import argparse

from src.train import train_model
from src.predict import predict, batch_predict
from src.utils import banner


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--train", action="store_true")
    parser.add_argument("--predict", type=float)
    parser.add_argument("--batch", action="store_true")

    args = parser.parse_args()

    if args.train:
        banner("TRAINING MODEL")
        train_model()

    elif args.predict is not None:
        banner("SINGLE PREDICTION")
        result = predict(args.predict)
        print(f"Predicted Marks: {result:.2f}")

    elif args.batch:
        banner("BATCH PREDICTION")

        values = input("Enter hours (comma separated): ")
        values = [float(x.strip()) for x in values.split(",")]

        results = batch_predict(values)

        for v, r in zip(values, results):
            print(f"{v} hours → {r:.2f}")

    else:
        print("""
Usage:

Train model:
    python -m src.main --train

Predict single:
    python -m src.main --predict 5

Batch:
    python -m src.main --batch
""")


if __name__ == "__main__":
    main()