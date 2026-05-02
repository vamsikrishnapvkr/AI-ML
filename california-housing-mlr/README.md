# California Housing Price Prediction using Multiple Linear Regression

## Problem Statement

The goal of this project is to predict housing prices in California using multiple input features such as median income, number of rooms, population, and location data.

We apply **Multiple Linear Regression (MLR)** to model the relationship between these features and the house price.

---

## Dataset

- Source: Scikit-learn California Housing Dataset
- Features:
  - MedInc (Median Income)
  - HouseAge
  - AveRooms
  - AveBedrms
  - Population
  - AveOccup
  - Latitude
  - Longitude

- Target:
  - House Price

---

## Approach

1. Load dataset from sklearn
2. Perform basic EDA (correlation analysis)
3. Split dataset into training and testing sets
4. Apply **StandardScaler** for feature scaling
5. Train a **Multiple Linear Regression** model
6. Evaluate using regression metrics:
   - MSE
   - RMSE
   - MAE
   - R² Score
   - Adjusted R²
7. Save model and scaler using pickle

---

## Results

| Metric | Value |
|--------|------|
| MSE | 0.5522 |
| RMSE | 0.7431 |
| MAE | 0.5371 |
| R² Score | 0.5936 |
| Adjusted R² | 0.5931 |

---

## Interpretation

- The model explains **~59.36% of the variance** in housing prices.
- RMSE (~0.74) indicates moderate prediction error.
- MAE (~0.53) shows average deviation from actual prices.
- Adjusted R² is very close to R², indicating relevant features.

---

## Limitations

- Linear regression assumes a linear relationship, but housing data is often non-linear.
- Model shows signs of **underfitting**.
- Cannot capture complex feature interactions.

---

## Conclusion

This project demonstrates that Multiple Linear Regression can serve as a **baseline model** for predicting housing prices.

While the model captures general trends, its performance is moderate (R² ≈ 59%), indicating that more advanced models like Random Forest or Gradient Boosting could significantly improve accuracy.

---

## How to Run

```bash
pip install -r requirements.txt
cd src
python train.py
python predict.py