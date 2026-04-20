import pandas as pd

from src.preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.prediction import train_waiting_time_model

# Load dataset
df = load_data("data/charging_ev_and_grid_optimization_dataset.csv")

# Clean
df = clean_data(df)

# Feature engineering
df = create_features(df)

# Train model
train_waiting_time_model(df)