from sklearn.linear_model import Ridge

# What is alpha?
# - Regularization strength
# - Higher alpha → simpler model → less overfitting
def build_model(alpha=1.0):
    # Create a Ridge regression model with the specified alpha
    # alpha is the regularization strength; must be a positive float. 
    # Regularization improves the conditioning of the problem and reduces the variance of the estimates. 
    # Larger values specify stronger regularization.
    # The default value is 1.0, which means that the regularization term will be added to the loss function with a weight of 1.0.
    
    model = Ridge(alpha=alpha)
    return model
