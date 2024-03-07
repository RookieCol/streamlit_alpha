
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import streamlit as st
import pandas as pd
from utils.displaying_data import display_stock_data
import yfinance as yf

st.title('Stock Data Visualization')
ticker_symbol = st.text_input('Enter ticker symbol', value='AAPL')
# User choice between plot and table
display_option = st.radio("Display as", ('Plot', 'Table'))
# Inputs for date range
start_date = st.date_input("Start date", value=pd.to_datetime('2023-01-01'))
end_date = st.date_input("End date", value=pd.to_datetime('2023-03-01'))

 # If a symbol is entered, fetch and display important info in the sidebar
if ticker_symbol:
    data = yf.Ticker(ticker_symbol).info
    st.sidebar.write(f"**Company:** {data['longName']}")
    st.sidebar.write(f"**Symbol:** {data['symbol']}")
    st.sidebar.write(f"**Current Price:** ${data['currentPrice']:.2f}")

    # Display price change information only if previous close is available
    if 'previousClose' in data:
        price_change = data['currentPrice'] - data['previousClose']
        change_percent = (price_change / data['previousClose']) * 100
        st.sidebar.write(f"**Change:** ${price_change:.2f} ({change_percent:.1f}%)")
        st.sidebar.write(f"**Market Cap:** ${data['marketCap']:,.0f}")

        

def plot_stock_data(ticker_symbol, start_date, end_date):
    try:
        # Fetching data
        stock = yf.Ticker(ticker_symbol)
        data = stock.history(interval='1d', start=start_date, end=end_date)
        
        if data.empty:
            st.error(f"No data found for {ticker_symbol} on the specified dates.")
            return
        
        # Preparing data for candlestick chart
        data['Date'] = data.index.map(mdates.date2num)
        ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']].copy()
        
        # Calculating moving averages
        data['MA5'] = data['Close'].rolling(window=5).mean()
        data['MA20'] = data['Close'].rolling(window=20).mean()
        
        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plotting candlestick chart
        candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
        
        # Plotting moving averages
        ax.plot(data['Date'], data['MA5'], color='blue', label='5-day moving average')
        ax.plot(data['Date'], data['MA20'], color='orange', label='20-day moving average')
        
        # Formatting Date
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        fig.autofmt_xdate()
        
        plt.title(f"{ticker_symbol} Stock Price")
        plt.legend()
        plt.grid(True)
        
        # Use Streamlit to display the plot
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Button to trigger the display based on the selected option
if st.button('Show Data'):
    if display_option == 'Table':
        display_stock_data(ticker_symbol, start_date, end_date)
    elif display_option == 'Plot':
        plot_stock_data(ticker_symbol, start_date, end_date)
