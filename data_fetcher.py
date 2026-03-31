import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_market_data(ticker):
    print(f"Fetching data for {ticker}...")
    
    # 1. Download data (1 year for better volatility calculation)
    data = yf.download(ticker, period="1y", auto_adjust=True)
    
    # 2. Fix the MultiIndex issue (if it exists)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # 3. Calculate Daily Returns
    # .pct_change() calculates (Price_today / Price_yesterday) - 1
    data['Returns'] = data['Close'].pct_change()

    # 4. Calculate Annualized Volatility
    # We multiply by sqrt(252) because there are 252 trading days in a year
    volatility = data['Returns'].std() * np.sqrt(252)
    print(f"\n--- Statistics for {ticker} ---")
    print(f"Annualized Volatility: {volatility:.2%}")

    # 5. Save to CSV
    data.to_csv('market_data.csv')
    print("Success! 'market_data.csv' has been updated.")

    # 6. Create and save a Price Chart
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', linewidth=1.5)
    plt.title(f'{ticker} Price History (Past 1 Year)', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Save the chart as an image
    plt.savefig('price_chart.png')
    print("Chart saved as 'price_chart.png'")
    
    # This will open a window showing the chart
    plt.show()

if __name__ == "__main__":
    # You can change this to any NSE ticker, e.g., "TCS.NS" or "HDFCBANK.NS"
    get_market_data("RELIANCE.NS") 