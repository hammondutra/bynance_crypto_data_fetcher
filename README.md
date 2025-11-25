# Binance Crypto Data Fetcher

A collection of Python scripts and notebooks for fetching cryptocurrency data from the Binance API and performing financial analysis.

## About This Project

This project provides tools to connect to the Binance cryptocurrency exchange API, download market data, and perform analysis. It currently includes a Jupyter Notebook for data fetching and a Python script for running Monte Carlo simulations, which can be used for financial modeling or risk assessment.

---

## Features

* **Binance API Integration:** A Jupyter Notebook (`Bynance_API_Fetch.ipynb`) demonstrating how to fetch data from the Binance API.
* **Financial Modeling:** A script (`Mock_Monte_Carlo.py`) for running mock Monte Carlo simulations, likely for price prediction or risk analysis.

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need Python 3.x installed on your system. You will also need several Python libraries, which can be installed via `pip`.

* [Python 3](https://www.python.org/downloads/)
* [Jupyter Notebook or Jupyter Lab](https://jupyter.org/install)

You will likely need the following libraries (or similar):
```bash
pip install pandas numpy requests jupyterlab
```
---

## Installation
1. Clone the repo:
```bash
git clone [https://github.com/hammondutra/bynance_crypto_data_fetcher.git](https://github.com/hammondutra/bynance_crypto_data_fetcher.git)
```

2. Navigate to the project directory:
```bash
cd bynance_crypto_data_fetcher
```

3. Install any required packages:
```bash
pip install -r requirements.txt
```

---

## Usage
1. Fetching Data
The `Bynance_API_Fetch.ipynb` notebook contains the code for fetching data.

* Start Jupyter Lab:
```bash
jupyter lab
```

* Open the `Bynance_API_Fetch.ipynb` notebook in your browser.

* Follow the steps in the notebook to connect to the API and download the cryptocurrency data.

---

## Monte Carlo Simulation
The `Mock_Monte_Carlo.py` script can be run from the command line.
```Bash
python Mock_Monte_Carlo.py
```

---

## Contributing
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m "Add some AmazingFeature"`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
