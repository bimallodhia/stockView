import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("stocks.csv")
symbols = df["symbol"].tolist()

plt.figure(figsize=(10, 6))

for symbol in symbols:
    stock = yf.Ticker(symbol)

    # Get last 30 days of price data
    hist = stock.history(period="1mo")

    if hist.empty:
        print(f"No data for {symbol}")
        continue

    plt.plot(hist.index, hist["Close"], label=symbol)

# Graph formatting
plt.title("Stock Price Trends (Last 30 Days)")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show graph
plt.show()
