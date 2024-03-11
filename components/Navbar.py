import streamlit as st
import yfinance as yf

def navbar():
    st.sidebar.title('Stocky ')
    
    symbol = st.session_state.symbol if 'symbol' in st.session_state else None

    if symbol:
        try:  # Error handling for potential API issues
            data = yf.Ticker(symbol).info
            st.sidebar.write(f"**Company:** {data['longName']}")
            st.sidebar.write(f"**Symbol:** {data['symbol']}")
            st.sidebar.write(f"**Current Price:** ${data['currentPrice']:.2f}")

            # Display price change information only if previous close is available
            if 'previousClose' in data:
                price_change = data['currentPrice'] - data['previousClose']
                change_percent = (price_change / data['previousClose']) * 100
                st.sidebar.write(f"**Change:** ${price_change:.2f} ({change_percent:.1f}%)")
                st.sidebar.write(f"**Market Cap:** ${data['marketCap']:,.0f}")
        except Exception as e:
            st.sidebar.error(f"Error fetching data for {symbol}: {e}")

