import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def run_monte_carlo(tickers, weights, days=252, simulations=10000):
    # 1. Load Data
    data = yf.download(tickers, period="1y", auto_adjust=True)['Close']
    returns = data.pct_change().dropna()
    
    # 2. Calculate Mean and Covariance
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    
    # 3. Setup Simulation
    portfolio_sims = np.full((days, simulations), 0.0)
    initial_portfolio_value = 1000000 # Assume a 10 Lakh INR Portfolio
    
    for i in range(simulations):
        # Cholesky Decomposition for correlated random variables
        Z = np.random.normal(size=(days, len(tickers)))
        L = np.linalg.cholesky(cov_matrix)
        daily_returns = mean_returns.values + np.dot(L, Z.T).T
        
        # Accumulate returns over the year
        portfolio_sims[:, i] = np.cumprod(np.dot(daily_returns, weights) + 1) * initial_portfolio_value

    # 4. Visualization
    plt.figure(figsize=(10,6))
    plt.plot(portfolio_sims[:, :100]) # Plot first 100 paths
    plt.axhline(initial_portfolio_value, color='r', linestyle='--', label='Initial Value')
    plt.title(f"Monte Carlo: 10,000 Potential Paths for {tickers}")
    plt.xlabel("Days")
    plt.ylabel("Portfolio Value (INR)")
    plt.legend()
    plt.savefig('monte_carlo_paths.png')
    plt.show()

    # 5. Risk Metrics (VaR)
    ending_values = portfolio_sims[-1, :]
    var_95 = np.percentile(ending_values, 5)
    print(f"95% Confidence Value at Risk (VaR): INR {initial_portfolio_value - var_95:,.2f}")

if __name__ == "__main__":
    assets = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
    weights = np.array([0.33, 0.33, 0.34])
    run_monte_carlo(assets, weights)