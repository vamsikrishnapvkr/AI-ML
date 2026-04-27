from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the performance of the Ridge Regression model on the test set.
    Parameters:
    model: The trained Ridge Regression model.
    X_test: The test features.
    y_test: The true target values for the test set.
    Returns:
    A dictionary containing the Mean Squared Error and R-squared score of the model.

    """
    # Predict the target values for the test set
    y_pred = model.predict(X_test)
    
    # Calculate Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    
    # Calculate R-squared score
    r2 = r2_score(y_test, y_pred)
    
    predictions =  {
        'Mean Squared Error': mse,
        'R-squared Score': r2
    }
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared Score: {r2}")
    return predictions
