from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Why scaling?
# Ridge uses L2 penalty, which is sensitive to feature magnitude.
def pre_process_data(df):
    # Separate features and target variable
    X = df.drop('MedHouseVal', axis=1)  # Features
    y = df['MedHouseVal']  # Target variable

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Standardize the features (mean=0, variance=1)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)  # Fit on training data and transform
    X_test_scaled = scaler.transform(X_test)  # Transform test data using the same scaler

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler