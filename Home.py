import streamlit as st
import yfinance as yf

def main():
    st.sidebar.title('Stock Data Visualization')
    
    # Input for ticker symbol in the sidebar
    symbol = st.sidebar.text_input("Enter a stock symbol", "AAPL")
    
    # If a symbol is entered, fetch and display important info in the sidebar
    if symbol:
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

# Main function call
if __name__ == "__main__":
    main()
