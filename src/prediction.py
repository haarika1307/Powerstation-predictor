import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def train_waiting_time_model(df):
    features = [
        'queue_length',
        'station_load',
        'charging_power_kW',
        'hour',
        'is_peak'
    ]

    X = df[features]
    y = df['waiting_time']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, preds))

    joblib.dump(model, "models/wait_model.pkl")

    return model