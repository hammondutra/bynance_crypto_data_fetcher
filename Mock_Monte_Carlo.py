"""
Simulate GBM asset price paths and visualize with matplotlib.
Outputs simple descriptive statistics for terminal prices.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from pathlib import Path

# Parameters (tweak freely)
S0 = 100.0     # initial price
mu = 0.06      # drift (annualized)
sigma = 0.25   # volatility (annualized)
T = 1.0        # years
steps = 252    # trading days
n_paths = 50   # number of paths
seed = 42      # RNG seed

def simulate_gbm_paths(S0, mu, sigma, T, steps, n_paths, seed=None):
    """Simulate GBM price paths and return time grid and path matrix."""
    rng = np.random.default_rng(seed)
    dt = T / steps
    Z = rng.standard_normal((steps, n_paths))
    dW = np.sqrt(dt) * Z
    drift = (mu - 0.5 * sigma**2) * dt
    incr = drift + sigma * dW
    log_paths = np.vstack([np.zeros((1, n_paths)), np.cumsum(incr, axis=0)])
    paths = S0 * np.exp(log_paths)
    t = np.linspace(0.0, T, steps + 1)
    return t, paths

def main():
    t, paths = simulate_gbm_paths(S0, mu, sigma, T, steps, n_paths, seed)

    # ---- Visualization: each path in a different color (matplotlib default cycle) ----
    plt.figure(figsize=(9, 5))
    plt.plot(t, paths)                    # no explicit colors -> distinct default colors
    plt.title("Mock Monte Carlo: GBM Asset Price Paths")
    plt.xlabel("Time (years)")
    plt.ylabel("Price")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    out_png = Path("asset_price_paths.png")
    plt.savefig(out_png, dpi=150)
    print(f"Saved plot -> {out_png.resolve()}")

    # ---- Simple descriptive statistics of terminal prices ----
    terminal = paths[-1, :]
    mean_terminal = float(np.mean(terminal))
    std_terminal  = float(np.std(terminal, ddof=1))
    p05, p50, p95 = [float(np.percentile(terminal, q)) for q in (5, 50, 95)]
    min_t, max_t  = float(np.min(terminal)), float(np.max(terminal))

    print("=== Descriptive Statistics (Terminal Prices) ===")
    print(f"Paths: {n_paths}, Steps: {steps}, Horizon: {T}y")
    print(f"Initial Price S0: {S0:.2f}, Drift mu: {mu:.2%}, Volatility sigma: {sigma:.2%}")
    print(f"Mean: {mean_terminal:.4f}")
    print(f"Std Dev: {std_terminal:.4f}")
    print(f"Min / Max: {min_t:.4f} / {max_t:.4f}")
    print(f"Median (p50): {p50:.4f}")
    print(f"p05 / p95: {p05:.4f} / {p95:.4f}")

if __name__ == "__main__":
    main()

