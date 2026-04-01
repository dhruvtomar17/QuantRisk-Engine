# QuantRisk-Engine: Automated NSE Market Analytics 

A quantitative toolkit developed to bridge the gap between abstract mathematical theory and actionable investment strategy. This project automates market data retrieval, performs multi-asset risk assessments, and utilizes stochastic modeling to identify "Fat Tail" risks in the Indian equity market.

## Key Features & Methodologies

### 1. Multi-Asset Portfolio Strategy & Optimization
Applied **Modern Portfolio Theory (MPT)** to develop a balanced allocation model across key sectors (Energy, IT, Banking).
- **Correlation Integrity:** Utilized an annualized covariance matrix to map inter-asset dynamics and identify natural sector hedges to mitigate systemic concentration risk.
- **Risk-Adjusted Performance:** Automated the calculation of the **Sharpe Ratio** to evaluate if expected returns justify the portfolio's volatility.

### 2. Market Risk Diagnostic & VaR Modeling
Engineered a diagnostic tool to measure the exposure of high-weight Nifty 50 constituents, such as RELIANCE.NS, TCS.NS, and HDFCBANK.NS.
- **Monte Carlo Simulations:** Executed 10,000 simulations to plot potential future price paths and account for extreme market volatility often underestimated by standard normal distributions.
- **Value at Risk (VaR):** Calculated VaR at a **95% confidence interval** to determine the minimum expected loss during market downturns.

### 3. Data Visualization & Empirical Modeling
- **Asset Correlation Matrix:** Visualized via Seaborn heatmaps to identify concentration risks.
- **Time-Series Analysis:** Generated historical price charts to identify volatility trends.
- **Stochastic Path Visualization:** Created "spaghetti plots" to demonstrate the distribution of potential portfolio outcomes over a 252-day trading year.

## 🛠 Tech Stack & Mathematical Foundation
- **Languages:** Python (NumPy, Pandas, Matplotlib, Seaborn, yfinance).
- **Math & Stats:** Linear Algebra (Matrix Operations, Cholesky Decomposition), Probability Distributions, and Statistical Inference.

## Sample Visualizations
- **Price Trend Analysis:** `price_chart.png`
- **Sector Correlation Heatmap:** `correlation_heatmap.png`
- **Stochastic Risk Simulation:** `monte_carlo_paths.png`

## Academic Alignment
This project serves as a practical implementation of the analytical training from my **B.Sc. Mathematics Honors** degree. It demonstrates proficiency in translating complex variables into defensible, risk-adjusted insights suitable for professional risk assessment and strategy roles.
