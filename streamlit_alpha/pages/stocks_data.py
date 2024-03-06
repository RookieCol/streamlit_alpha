import streamlit as st
from utils.data_fetcher import fetch_stock_data

def app():
    st.title('Stock Data')

    ticker_symbol = st.text_input('Enter ticker symbol', value='AAPL')
    # Additional input for time frame, etc.

    # Display data using fetched data
    # Example: stock_data = fetch_stock_data(ticker_symbol, start_date, end_date)
    # st.line_chart(stock_data)
