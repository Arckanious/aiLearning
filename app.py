import yfinance as yf
import pandas as pd

ticker = 'AAPL'

data = yf.download(ticker, period='5y', interval='1d')

#basic exploration
print(f"Data for {ticker}:")
print(data.head())

print(f"Data columns: {data.columns.tolist()}")
print(data.info())

print(f"Data shape: {data.shape}")
print(data.describe())

# Check for missing values
print("Missing values in each column:")
print(data.isnull().sum())

#Save CSV for offline use
data.to_csv(f'dataset/{ticker}_5y_data.csv')



