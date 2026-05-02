# src/predict.py

import pickle
import numpy as np

# Load model & scaler
model = pickle.load(open('../models/mlr_model.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))

# Example input (must match feature order)
sample = np.array([[8.3252, 41, 6.9841, 1.0238, 322, 2.5556, 37.88, -122.23]])

# Scale input
sample_scaled = scaler.transform(sample)

# Predict
prediction = model.predict(sample_scaled)

print("Predicted House Price:", prediction[0])