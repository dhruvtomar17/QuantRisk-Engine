import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_portfolio(tickers, weights):
    print(f"Analyzing Portfolio: {tickers}")
    
    # 1. Fetch data for multiple assets
    data = yf.download(tickers, period="1y", auto_adjust=True)['Close']
    
    # 2. Calculate Daily Returns
    returns = data.pct_change().dropna()
    
    # 3. Portfolio Returns (Weighted average of individual returns)
    portfolio_return = np.sum(returns.mean() * weights) * 252
    
    # 4. Portfolio Volatility (Risk) using Matrix Operations
    # This applies the formula: sqrt(W^T * Cov * W)
    cov_matrix = returns.cov() * 252
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_volatility = np.sqrt(portfolio_variance)
    
    # 5. Sharpe Ratio (Assuming 5% Risk-Free Rate)
    risk_free_rate = 0.05
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    
    print(f"\n--- Portfolio Results ---")
    print(f"Expected Annual Return: {portfolio_return:.2%}")
    print(f"Annualized Volatility: {portfolio_volatility:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

    # 6. Visualize Correlation Heatmap
    plt.figure(figsize=(8, 6))
    import seaborn as sns
    sns.heatmap(returns.corr(), annot=True, cmap='coolwarm')
    plt.title("Asset Correlation Matrix (Sector Hedging)")
    plt.savefig('correlation_heatmap.png')
    plt.show()

if __name__ == "__main__":
    # Defining a 3-sector portfolio (Energy, IT, Banking)
    assets = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
    # Equal weighting (33% each)
    user_weights = np.array([0.33, 0.33, 0.34])
    
    analyze_portfolio(assets, user_weights)