## Simple Linear Regression (scikit-learn)

End-to-end ML project with training, prediction, testing, and modular design.

---

## Project Structure
```text
    simple-linear-regression-sklearn/
    │
    ├── data/
    │   └── dataset.csv
    │
    ├── models/
    │   └── linear_model.pkl
    │
    ├── src/
    │   ├── config.py
    │   ├── main.py
    │   ├── model.py
    │   ├── predict.py
    │   ├── train.py
    │   └── utils.py
    │
    ├── tests/
    │   └── test_model.py
    │
    ├── requirements.txt
    └── README.md
```
---

## Setup

```bash
pip install -r requirements.txt
```

## Run Training
```bash
python -m src.main --train
```

## Run Prediction
```bash
python -m src.main --predict 6
```

## Batch prediction
```bash
python -m src.main --batch
```
input: 2,4,6,8

## Run Tests
### Windows
python -m pytest tests/

### Output Example
MSE: 4.32
R2 : 0.98

Predicted Marks: 55.23

## Concepts Covered
- Simple Linear Regression
- Train/test split
- Model evaluation
- Model persistence
- Unit testing
- CLI interface