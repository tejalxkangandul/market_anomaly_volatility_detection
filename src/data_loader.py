import yfinance as yf
import pandas as pd


def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Fetches historical market data from Yahoo Finance."""
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)

    if df.empty:
        raise ValueError("No data fetched. Check ticker or dates.")

    return df
