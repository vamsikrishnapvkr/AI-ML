from sklearn.datasets import fetch_california_housing
import pandas as pd

# We load dataset directly from sklearn
# Convert into a Pandas DataFrame
# Easier for Exploratory Data Analysis (EDA) and preprocessing
def load_data():
    # Load the California housing dataset
    data = fetch_california_housing(as_frame=True)
    # Convert the dataset to a pandas DataFrame
    df = data.frame
    return df