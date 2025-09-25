import yfinance as yf
import pandas as pd
import numpy as np

#Download historical data for Apple
ticker = "AAPL"
data = yf.download(ticker, period="5y", interval="1d")

print(data.head())
print(data.info())
print(data.describe())

print(data.isnull().sum())

data.to_csv("AAPL_5yr.csv")