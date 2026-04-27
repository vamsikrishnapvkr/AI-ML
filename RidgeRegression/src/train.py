import joblib

def train_model(model, X_train, y_train):
    # Train the model and save it to disk
    model.fit(X_train, y_train)
    # Save the trained model to a file
    # joblib is used for saving the model in a format that can be easily loaded later
    joblib.dump(model, "models/ridge_model.pkl")
    return model