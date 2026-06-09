import argparse
from src.data_loader import fetch_data
from src.features import engineer_features
from src.models.isolation_forest import train_and_predict_if
from src.visualization import plot_anomalies


def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description="Market Anomaly Detection Pipeline")
    parser.add_argument("--ticker", type=str, default="SPY",
                        help="Stock ticker to analyze")
    parser.add_argument("--start", type=str,
                        default="2019-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2023-12-31",
                        help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    # 1. Load Data
    raw_df = fetch_data(args.ticker, args.start, args.end)

    # 2. Feature Engineering
    features_df = engineer_features(raw_df)

    # 3. Model Training & Prediction
    results_df = train_and_predict_if(features_df, contamination=0.03)

    # 4. Visualization
    plot_anomalies(results_df, args.ticker)


if __name__ == "__main__":
    main()
