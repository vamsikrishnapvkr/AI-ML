# Polynomial Regression Project (End-to-End Machine Learning Pipeline)

## Project Summary

This project demonstrates an end-to-end Machine Learning workflow using **Polynomial Regression** to predict house prices using a real-world Kaggle dataset.

Dataset used:  
House Prices - Advanced Regression Techniques (Kaggle)

We cover:
- Non-linear regression modeling
- Underfitting vs overfitting
- Feature engineering using polynomial features
- Complete ML pipeline (download → preprocess → train → evaluate → visualize)

---

# Project Structure

```bash
polynomial-regression-project/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── download_data.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── visualize.py
│

```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/vamsikrishnapvkr/AI-ML.git
cd polynomial-regression-project
```

---

## Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Kaggle API

```bash
pip install kaggle
```

Place Kaggle API key:

```bash
~/.kaggle/kaggle.json
```

---

# How to Run Project (Step-by-Step)

## Step 1: Download Dataset

```bash
python src/download_data.py
```

---

## Step 2: Preprocess Data

```bash
python src/preprocess.py
```

---

## Step 3: Train Model

```bash
python src/train.py
```

---

## Step 4: Evaluate Model

```bash
python src/evaluate.py
```

Outputs:
- MSE
- R² Score

---

## Step 5: Visualize Results

```bash
python src/visualize.py
```

---

# Input Format

```python
X = [
  [8450, 7, 5, 2003]
]
```

(Example: area, rooms, quality, year built)

---

# Output Format

```text
Predicted House Price (USD)
```

Example:
```text
245000
```

---

# How to Test Project

## Full Pipeline

```bash
python src/download_data.py
python src/preprocess.py
python src/train.py
python src/evaluate.py
```

---

## Manual Prediction

```python
import joblib
import numpy as np

model = joblib.load("models/model.pkl")

sample = np.array([[8450, 7, 5, 2003]])
prediction = model.predict(sample)

print(prediction)
```

---

# requirements.txt

```txt
numpy
pandas
matplotlib
scikit-learn
joblib
kaggle
```

---

# Model Explanation

Polynomial Regression equation:

y = w0 + w1x + w2x² + w3x³ + ... + wnxⁿ

Degrees meaning:
- Degree 0 → constant model
- Degree 1 → linear
- Degree 2 → quadratic curve
- Degree 3+ → complex curves

---

# Underfitting vs Overfitting

| Degree | Behavior |
|--------|----------|
| 1 | Underfitting |
| 2–3 | Good fit |
| 10+ | Overfitting |

---

# Important Notes

- High polynomial degree may overfit
- Feature scaling improves stability
- Only numeric features used in baseline

---

# License

This project is for educational purposes only.