import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import streamlit as st

def plot_stock_data(data, ticker_symbol):
    try:
        data['Date'] = data.index.map(mdates.date2num)
        ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']].copy()
        data['MA5'] = data['Close'].rolling(window=5).mean()
        data['MA20'] = data['Close'].rolling(window=20).mean()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
        ax.plot(data['Date'], data['MA5'], color='blue', label='5-day moving average')
        ax.plot(data['Date'], data['MA20'], color='orange', label='20-day moving average')
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        fig.autofmt_xdate()
        
        plt.title(f"{ticker_symbol} Stock Price")
        plt.legend()
        plt.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")
