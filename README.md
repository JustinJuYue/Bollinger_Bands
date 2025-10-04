# 📈 Bollinger Bands Trading Signal Generator

This Python script downloads historical stock data for a specific ticker (default is **AAPL**), calculates **Bollinger Bands**, and generates potential **buy and sell signals** based on a simple crossover strategy. The results, including the stock price, Bollinger Bands, and trading signals, are visualized in a plot.

---

## 📜 Description

**Bollinger Bands** are a technical analysis tool consisting of three lines plotted in relation to a security's price:

- **Middle Band**: A Simple Moving Average (SMA) of the asset's price.
- **Upper Band**: Typically two standard deviations above the Middle Band.
- **Lower Band**: Typically two standard deviations below the Middle Band.

This script implements a common **mean-reversion strategy**:

- 🟢 **Buy Signal**: When the price crosses **below the Lower Band**, suggesting the asset may be **oversold**.
- 🔴 **Sell Signal**: When the price crosses **above the Upper Band**, suggesting the asset may be **overbought**.

---

## ✨ Features

- 📥 **Data Retrieval**: Fetches historical stock data from Yahoo Finance via `yfinance`.
- 📊 **Bollinger Bands Calculation**: Computes the SMA, Upper Band, and Lower Band.
- 📈 **Signal Generation**: Flags potential **buy/sell** signals when price crosses the bands.
- 🖼️ **Visualization**: Plots price data, Bollinger Bands, and trade signals using `matplotlib`.
- ⚙️ **Customizable Parameters**: Ticker symbol, date range, and Bollinger Band settings can be easily modified.

---

## ⚙️ Requirements

To run this script, you need **Python 3** and the following libraries:

- `matplotlib`
- `yfinance`
- `pandas` (installed with `yfinance`)
- `datetime` (standard Python library)

---

## 🚀 Installation & Usage

1. **Install the required libraries:**

```bash
pip install matplotlib yfinance pandas
```
2. **Run the script from your terminal:**
```bash
python main.py
```
The script will:

-Print a DataFrame showing price data and generated signals.
-Display a plot with Bollinger Bands and buy/sell markers.

## 🔧 Customization

You can change the analysis parameters at the top of the script:

**🔄 Change the Ticker**

```bash
# From:
data = yf.download("AAPL", start=start, end=end, auto_adjust=False)

# To (e.g., Microsoft):
data = yf.download("MSFT", start=start, end=end, auto_adjust=False)
```
**📏 Adjust Bollinger Bands Settings**
```bash
Modify the window and standard deviation to change the sensitivity of the bands:

bollinger_window = 20      # Lookback period for SMA
bollinger_std_dev = 2      # Standard deviations for upper/lower bands
```
📆 Change the Time Frame

To analyze a different historical period, modify the start and end date ranges:
```bash
# Analyze the last 5 years instead of 3
start = dt.datetime.now() - dt.timedelta(days=365*5)
end = dt.datetime.now()
```
## ⚠️ Disclaimer

This script is intended for educational and informational purposes only.
The trading signals generated are based on a simplistic technical analysis strategy and should not be considered financial advice.
Trading involves risk, and you should do your own research or consult a licensed financial advisor before making any investment decisions.

