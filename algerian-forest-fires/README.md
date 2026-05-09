# Algerian Forest Fires Prediction using Ridge Regression

## Project Overview

The objective of this project is to analyze the Algerian Forest Fires Dataset and build a Machine Learning model to predict the **Fire Weather Index (FWI)**.

The dataset contains meteorological and fire-related observations collected from two Algerian regions:

- **Bejaia Region**
- **Sidi Bel-Abbes Region**

This project includes:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering (FE)
- Correlation Analysis and Feature Selection
- Model Training using Ridge Regression
- Model Optimization using RidgeCV
- Saving trained artifacts for deployment

---

# Dataset Information

The dataset contains weather and fire-related attributes such as:

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- FFMC
- DMC
- DC
- ISI
- BUI
- FWI
- Classes (Fire / Not Fire)

## Target Variable

- **FWI (Fire Weather Index)**

---

# Project Workflow

## 1. Data Cleaning and Preprocessing

- Removed unnecessary columns
- Handled missing values
- Converted categorical variables into numerical format
- Changed data types where required
- Applied Standard Scaling before model training

---

## 2. Exploratory Data Analysis (EDA)

### Fire Distribution

- Dataset contains both:
  - Fire
  - Not Fire classes
- Fire occurrences are slightly higher in the **Sidi Bel-Abbes** region.

### Seasonal Trend

Most forest fires occurred during:

- June
- July
- August

August recorded the highest number of fires.

### Correlation Analysis

Important positively correlated features with **FWI**:

- Temperature
- FFMC
- DMC
- ISI

Features with correlation higher than **0.85** were removed to reduce multicollinearity.

### Outlier Analysis

- Boxplot analysis showed some outliers in the FWI feature.
- Standard Scaling helped normalize feature distributions before training.

---

# Model Training

## Ridge Regression

Ridge Regression was selected to handle multicollinearity and improve model generalization.

### Evaluation Metrics

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### Performance

The model achieved:

- Low prediction error
- High R² score indicating strong predictive performance

---

# RidgeCV Optimization

Hyperparameter tuning was performed using **RidgeCV**.

```python
alphas = np.logspace(-3, 3, 50)
```

- 5-Fold Cross Validation was used
- Best alpha value selected automatically

---

# Saved Artifacts

Trained model files:

- `ridge.pkl` → Trained Ridge Regression model
- `scaler.pkl` → StandardScaler object

---

# Project Structure

```bash
project/
│
├── notebooks/
│   ├── EDA_FE_Algerian_Forest_Fires.ipynb
│   └── Model_Training.ipynb
│
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
│
├── config/
│   └── Algerian_forest_fires_dataset_CLEANED.csv
|
├── templates/
│   └── home.html
│
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle

---

# Conclusion

This project demonstrates an end-to-end Machine Learning workflow for predicting the **Fire Weather Index (FWI)** using meteorological data.

## Key Achievements

- Performed detailed EDA and Feature Engineering
- Reduced multicollinearity using correlation analysis
- Built an optimized Ridge Regression model
- Achieved strong predictive performance
- Saved trained artifacts for future deployment


---

# Author

Developed as part of a Machine Learning regression project on Algerian Forest Fire prediction.
