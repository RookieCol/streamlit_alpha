import pandas as pd
import yfinance as yf

def fetch_stock_data(ticker_symbol, start_date, end_date):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(interval='1d', start=start_date, end=end_date)
    return data
