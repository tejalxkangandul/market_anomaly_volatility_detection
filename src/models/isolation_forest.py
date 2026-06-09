import pandas as pd
from sklearn.ensemble import IsolationForest


def train_and_predict_if(df: pd.DataFrame, contamination: float = 0.03) -> pd.DataFrame:
    """Trains Isolation Forest and flags anomalies."""
    print(f"Training Isolation Forest (Contamination: {contamination})...")
    features = ['Return', 'Volatility_21d', 'Momentum_21d']
    X = df[features]

    # Initialize and fit
    model = IsolationForest(
        n_estimators=100, contamination=contamination, random_state=42)
    model.fit(X)

    # Predict (-1 is anomaly, 1 is normal)
    df = df.copy()
    df['Anomaly'] = model.predict(X)

    return df
