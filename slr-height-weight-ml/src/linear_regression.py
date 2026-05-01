"""
Linear Regression: Height vs Weight Prediction

Goal:
Predict human height based on weight using simple linear regression.

Steps:
1. Load data
2. Visualize relationship
3. Train-test split
4. Feature scaling
5. Train model
6. Evaluate model
7. Predict new values
8. Residual analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("data/HeightWeight.csv")

print("First 5 rows:")
print(df.head())


# -----------------------------
# 2. Visualize data
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["Weight(Pounds)"], df["Height(Inches)"], alpha=0.5)
plt.title("Weight vs Height")
plt.xlabel("Weight (Pounds)")
plt.ylabel("Height (Inches)")
plt.show()


# -----------------------------
# 3. Split features
# -----------------------------
X = df[["Weight(Pounds)"]].values
y = df["Height(Inches)"].values


# -----------------------------
# 4. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -----------------------------
# 5. Feature scaling
# IMPORTANT: prevent data leakage
# -----------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -----------------------------
# 6. Train model
# -----------------------------
model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("\nModel trained successfully!")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)


# -----------------------------
# 7. Predictions
# -----------------------------
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)


# -----------------------------
# 8. Best fit line (test set)
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(X_test_scaled, y_test, alpha=0.5)
plt.plot(X_test_scaled, y_pred_test, color="red")
plt.title("Best Fit Line (Test Data)")
plt.xlabel("Scaled Weight")
plt.ylabel("Height")
plt.show()


# -----------------------------
# 9. Evaluation metrics
# -----------------------------
mse = mean_squared_error(y_test, y_pred_test)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

print("\nModel Performance:")
print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R² Score:", r2)


# -----------------------------
# 10. Adjusted R²
# -----------------------------
n = len(y_test)
k = X_test.shape[1]

adj_r2 = 1 - (1 - r2) * (n - 1) / (n - k - 1)
print("Adjusted R²:", adj_r2)


# -----------------------------
# 11. Predict new value
# -----------------------------
new_weight = np.array([[80]])
scaled_weight = scaler.transform(new_weight)

predicted_height = model.predict(scaled_weight)

print("\nPrediction:")
print(f"Height for 80 lbs: {predicted_height[0]:.2f} inches")


# -----------------------------
# 12. Residual analysis
# -----------------------------
residuals = y_test - y_pred_test

plt.figure(figsize=(6,4))
sns.histplot(residuals, kde=True)
plt.title("Residual Distribution")
plt.show()


plt.figure(figsize=(6,4))
plt.scatter(y_pred_test, residuals, alpha=0.5)
plt.axhline(0, color='red')
plt.title("Residuals vs Predictions")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.show()