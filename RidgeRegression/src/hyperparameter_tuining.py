from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Why do we need hyperparameter tuning?
# Hyperparameter tuning is essential for optimizing the performance of machine learning models.

def hyperparameter_tuning(X_train, y_train):
    """
    Performs hyperparameter tuning for the Ridge Regression model using GridSearchCV.
    Parameters:
    X_train: The training features.
    y_train: The training target values.
    Returns:
    The best Ridge Regression model found by GridSearchCV.

    """
    # Define the Ridge Regression model
    ridge = Ridge()

    # Define the hyperparameters to tune
    # alpha: Regularization strength (higher values specify stronger regularization)
    # solver: The solver to use in the computational routines
    param_grid = {
        'alpha': [0.1, 1.0, 10.0, 100.0],  # Regularization strength
        'solver': ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']  # Solvers to use
    }

    # Perform GridSearchCV to find the best hyperparameters
    grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, cv=5)
    grid_search.fit(X_train, y_train)

    # Print the best hyperparameters
    print(f"Best Hyperparameters: {grid_search.best_params_}")

    best_model = grid_search.best_estimator_
    print(f"Best Model: {best_model}")

    # Return the best model
    return best_model