# pip install matplotlib datetime yfinance

import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf

# Define the parameters for the Bollinger Bands
bollinger_window = 20
bollinger_std_dev = 2

# Set the time frame for data retrieval
start = dt.datetime.now() - dt.timedelta(days=365*3)
end = dt.datetime.now()

# Download historical stock data
data = yf.download("AAPL", start=start, end=end, auto_adjust=False)

# Calculate the Middle Band (Simple Moving Average)
data[f'SMA_{bollinger_window}'] = data['Adj Close'].rolling(window=bollinger_window).mean()

# Calculate the Standard Deviation
data['STD'] = data['Adj Close'].rolling(window=bollinger_window).std()

# Calculate the Upper and Lower Bands
data['Upper'] = data[f'SMA_{bollinger_window}'] + (data['STD'] * bollinger_std_dev)
data['Lower'] = data[f'SMA_{bollinger_window}'] - (data['STD'] * bollinger_std_dev)

# Remove the initial rows with NaN values
data = data.iloc[bollinger_window:]

# --- Generate Trading Signals ---
buy_signals = []
sell_signals = []

for x in range(len(data)):
    # A potential buy signal occurs when the price crosses below the lower band
    if data['Adj Close'].iloc[x] < data['Lower'].iloc[x]:
        buy_signals.append(data['Adj Close'].iloc[x])
        sell_signals.append(float('nan'))
    # A potential sell signal occurs when the price crosses above the upper band
    elif data['Adj Close'].iloc[x] > data['Upper'].iloc[x]:
        buy_signals.append(float('nan'))
        sell_signals.append(data['Adj Close'].iloc[x])
    else:
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))

data['Buy Signals'] = buy_signals
data['Sell Signals'] = sell_signals

print(data)

# --- Plotting the Data and Bollinger Bands ---
plt.figure(figsize=(14, 7))
plt.plot(data['Adj Close'], label='Share Price', alpha=0.6)
plt.plot(data['Upper'], label='Upper Band', color='cyan', linestyle='--')
plt.plot(data[f'SMA_{bollinger_window}'], label=f'SMA {bollinger_window} (Middle Band)', color='orange', linestyle='--')
plt.plot(data['Lower'], label='Lower Band', color='purple', linestyle='--')
plt.fill_between(data.index, data['Upper'], data['Lower'], color='grey', alpha=0.1)

plt.scatter(data.index, data['Buy Signals'], label='Buy Signal', marker='^', color='green', s=100)
plt.scatter(data.index, data['Sell Signals'], label='Sell Signal', marker='v', color='red', s=100)

plt.title('AAPL Bollinger Bands')
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.legend(loc='upper left')
plt.show()