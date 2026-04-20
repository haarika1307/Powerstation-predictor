import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Convert datetime columns
    time_cols = [
        "timestamp",
        "arrival_time",
        "charging_start_time",
        "charging_end_time"
    ]

    for col in time_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(method='ffill')

    return df