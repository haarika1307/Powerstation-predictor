def create_features(df):
    # Time features
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day

    # Peak encoding
    df['is_peak'] = df['time_slot'].apply(lambda x: 1 if x == "Peak" else 0)

    # Charging required
    df['charging_needed'] = (
        (df['final_soc'] - df['initial_soc']) * df['battery_capacity_kWh'] / 100
    )

    # Efficiency
    df['wait_efficiency'] = df['waiting_time'] / (df['queue_length'] + 1)

    return df