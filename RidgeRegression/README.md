## Predicting house prices using features like:
- Median income
- House age
- Number of rooms
- Population

## Why Ridge Regression?
- Handles multicollinearity
- Prevents overfitting
- Adds L2 regularization

## Key Concepts Explained
- Ridge Regression Formula
    - $Loss=RSS + \lambda\sum w^2$
- This is based on L2 Regularization
- Why Ridge Works
    - Shrinks coefficients instead of eliminating them
    - Handles multicollinearity
    - Reduces model variance

# Ridge Regression Project

## Objective
Predict housing prices using Ridge Regression.

## Dataset
California Housing Dataset

## Steps
- Data Loading
- EDA
- Preprocessing
- Model Training
- Evaluation

## Results
R2 Score: ~0.6–0.7

## How to run
```bash
pip install -r requirements.txt
python main.py
```