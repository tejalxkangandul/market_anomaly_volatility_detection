# Market Anomaly & Volatility Detection Pipeline

This project is a time-series and statistical modeling tool that automatically analyzes historical stock market data to flag high-risk, unpredictable market days (called **tail-risk events**) and differentiate them from normal trading regimes.

The pipeline is used to backtest model performance over two massive historical macroeconomic crises: the **2020 COVID-19 Market Crash** and the **2022 Federal Reserve Rate Hike Period**. Demonstrating these skills is directly relevant to quantitative research, market risk, and Value at Risk (VaR) estimation roles.

---

## 💡 How the Model Works (In Simple Words)

The core brain of this project is an unsupervised machine learning algorithm called an **Isolation Forest**.

Instead of trying to learn what a "normal" day looks like, the model isolates unusual data points by randomly picking a market feature and randomly splitting its value. Think of it like playing a game of **"20 Questions"** to isolate a specific day:

- **Normal, Boring Days:** They all cluster tightly together. To isolate a single normal day, the model has to ask a long string of highly specific questions.
- **Tail-Risk Days (Anomalies):** They sit completely alone away from the crowd. The model can isolate them almost instantly with only 1 or 2 structural questions (e.g., _"Did the market drop by more than 7% today? Yes."_).

Because true market anomalies require significantly fewer splits to be isolated, the model easily flags them as tail-risk events and marks them on your chart.

---

## 📂 Technologies Used & Their Purpose

| Technology                        | Purpose                                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------------------- |
| `yfinance` (Yahoo Finance API)    | Dynamically pulls historical stock and index price data (e.g., the S&P 500 / SPY).           |
| `Pandas`                          | Cleans tabular data and handles advanced time-series mathematics.                            |
| `Scikit-Learn` (Isolation Forest) | Handles the mathematical modeling and unsupervised anomaly detection logic.                  |
| `Plotly`                          | Powers the interactive, visual risk dashboard to inspect volatility spikes.                  |
| `PyTorch`                         | Included as a future architecture placeholder to upgrade the project to an LSTM Autoencoder. |

---

## 🗺️ Project Workflow

```
[1. Fetch Data] ──────> [2. Feature Engineering] ──────> [3. Isolation Forest] ──────> [4. Plotly Dashboard]

Pulls raw historical      Calculates returns,              Plays "20 Questions" to       Saves a visual, interactive
prices via yfinance API.  momentum, and annualized          isolate tail-risk events.     HTML dashboard file.
                          volatility.
```

---

## ⚙️ Financial Feature Engineering

Rather than feeding raw stock prices straight into the model, this pipeline mathematically processes the time-series data to match standard institutional quant data preparation:

- **Daily Returns:** Tracks the percentage change of the close price day-over-day.
- **Rolling Momentum:** Measures standard 21-day (approx. 1 trading month) price directional momentum.
- **Annualized Volatility:** Converts short-term daily volatility into a standard annual metric using the quantitative formula


---

## 🚀 Step-by-Step Execution Instructions

This project is built with a clean, modular software architecture that makes it reusable, maintainable, and easy to deploy. Follow these steps in your terminal to run it locally:

### Step 1: Open Your Terminal

Navigate into your main project workspace folder:

```powershell
cd market_anomaly_detection
```

### Step 2: Initialize a Safe Virtual Environment

Creating an isolated environment keeps your project dependencies clean and stable:

```powershell
python -m venv venv
```

### Step 3: Activate Your Virtual Environment

Activate the environment so your terminal runs within this isolated bubble:

```powershell
.\venv\Scripts\Activate.ps1
```

> You will see a green `(venv)` tag appear at the very left of your prompt line.

### Step 4: Install Dependencies (Windows Security Bypass)

Windows Application Control or AppLocker security policies often block raw local `.exe` files like `pip.exe`. To cleanly bypass this block, use modern, pre-compiled library versions and run the module installer through the trusted system Python executable directly:

```powershell
python -m pip install -r requirements.txt
```

### Step 5: Execute the Pipeline

Run the main entry script to fetch data, process metrics, train the model, and save your visual backtest:

```powershell
python main.py
```

---

## 🔍 Understanding & Interpreting the Output

When execution finishes, the pipeline exports a self-contained interactive web file named `anomaly_dashboard.html`. Opening this file in any browser reveals a clear visualization of two totally different types of historical market stress:

### 1. The 2020 COVID Crash (Acute Tail-Risk Event) ⚡

- **The Environment:** The market suffered an immediate, vertical drop. Annualized rolling volatility instantly exploded from a flat baseline up to nearly **90%**.
- **The Model Result:** Because these days saw extreme, sudden negative price drops, they were incredibly easy for the model to isolate. The Isolation Forest correctly identifies this as a **black-swan price shock** and covers the bottom of the crash in flagged markers.

### 2. The 2022 Rate Hikes (Sustained Volatility Regime Shift) 🌧️

- **The Environment:** Driven by systematic Federal Reserve interest rate hikes, the market spent 12 months grinding downward in an orderly fashion. Volatility established a steady, elevated baseline of **20% to 30%**.
- **The Model Result:** While the market was down, the day-over-day price adjustments were steady rather than sudden flash-crash anomalies. The model successfully avoids over-flagging this period, correctly identifying that high volatility had simply become the **new normal structural regime** rather than a series of disconnected daily surprises.

---

## 🔮 Model Limitations & Next Steps

While highly effective for tabular data, a core limitation of the Isolation Forest is that it treats every single trading day as an **independent observation** — it does not natively understand data sequence or time memory.

The logical next step to elevate this pipeline to institutional-grade detection is integrating a **PyTorch LSTM Autoencoder**, which learns temporal sequences and flags complex anomalies based on spikes in sequence reconstruction errors.
