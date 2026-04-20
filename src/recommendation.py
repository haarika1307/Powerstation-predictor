import joblib
import pandas as pd

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "wait_model.pkl")

model = joblib.load(MODEL_PATH)


def recommend_station(df, user_input, mode="fast"):
    df_copy = df.copy()

    features = [
        'queue_length',
        'station_load',
        'charging_power_kW',
        'hour',
        'is_peak'
    ]

    df_copy['predicted_wait'] = model.predict(df_copy[features])

    # Cost calculation
    df_copy['cost'] = df_copy['energy_consumed_kWh'] * df_copy['electricity_price']

    # Scoring
    if mode == "fast":
        df_copy['score'] = df_copy['predicted_wait']

    elif mode == "cheap":
        df_copy['score'] = df_copy['cost']

    elif mode == "eco":
        df_copy['score'] = -df_copy['renewable_energy_ratio']

    best = df_copy.sort_values('score').iloc[0]

    return best[['station_id', 'predicted_wait', 'cost', 'renewable_energy_ratio']]