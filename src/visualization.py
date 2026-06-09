import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


def plot_anomalies(df: pd.DataFrame, ticker: str):
    """Generates an interactive Plotly dashboard and saves it as an HTML file."""
    print("Generating interactive dashboard...")
    anomalies = df[df['Anomaly'] == -1]

    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
        subplot_titles=(
            f"{ticker} Price & Detected Tail-Risk Anomalies", "Annualized 21-Day Volatility"),
        row_heights=[0.7, 0.3]
    )

    # Price and Anomalies
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price', line=dict(
        color='blue', width=1)), row=1, col=1)
    fig.add_trace(go.Scatter(x=anomalies.index, y=anomalies['Close'], mode='markers', name='Anomaly', marker=dict(
        color='red', size=6, symbol='x')), row=1, col=1)

    # Volatility
    fig.add_trace(go.Scatter(x=df.index, y=df['Volatility_21d'], mode='lines', name='Volatility', line=dict(
        color='orange', width=1)), row=2, col=1)

    # Macro Overlays
    fig.add_vrect(x0="2020-02-19", x1="2020-04-10", fillcolor="red", opacity=0.1,
                  line_width=0, annotation_text="COVID Crash", row='all', col=1)
    fig.add_vrect(x0="2022-03-01", x1="2022-12-31", fillcolor="gray", opacity=0.1,
                  line_width=0, annotation_text="2022 Rate Hikes", row='all', col=1)

    fig.update_layout(
        title=f"Market Anomaly & Volatility Detection ({ticker})", height=800, template="plotly_white", hovermode="x unified")

    # --- THE FIX ---
    output_file = "anomaly_dashboard.html"
    fig.write_html(output_file)
    print(f"Dashboard saved successfully to: {os.path.abspath(output_file)}")
    # ----------------
