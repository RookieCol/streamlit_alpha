import streamlit as st
import pandas as pd
from utils.data_fetcher import fetch_stock_data
from utils.data_visualizer import plot_stock_data

st.title('Stock Data Visualization')
ticker_symbol = st.text_input('Enter ticker symbol', value='AAPL')
start_date = st.date_input("Start date", value=pd.to_datetime('2023-01-01'))
end_date = st.date_input("End date", value=pd.to_datetime('today'))

if st.button('Consult'):
    data = fetch_stock_data(ticker_symbol, start_date, end_date)
    
    if data.empty:
        st.error(f"No data found for {ticker_symbol} on the specified dates.")
    else:
        st.write("## Stock Data:")
        st.write(data)
        
        st.write("## Stock Chart:")
        plot_stock_data(data, ticker_symbol)
