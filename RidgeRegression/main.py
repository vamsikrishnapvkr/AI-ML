from src.data_loader import load_data
from src.preprocessing import pre_process_data
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.hyperparameter_tuining import hyperparameter_tuning

def main():
    # Load data
    df = load_data()

    # Preprocess data
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = pre_process_data(df)

    # build model
    model = build_model(alpha=1.0)

    # Train model
    trained_model = train_model(model, X_train_scaled, y_train)

    # Evaluate model
    predictions = evaluate_model(trained_model, X_test_scaled, y_test)

    # Hyperparameter tuning
    best_model = hyperparameter_tuning(X_train_scaled, y_train)
    # Evaluate the best model
    best_predictions = evaluate_model(best_model, X_test_scaled, y_test)


if __name__ == "__main__":
    main()