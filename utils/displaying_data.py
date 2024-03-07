import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime

def unix_timestamp_to_date(timestamp):
    """Converts a Unix timestamp to a human-readable date."""
    if timestamp is None or timestamp == 'N/A':
        return 'N/A'
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

def display_stock_data(ticker_symbol, start_date, end_date):
    try:
        stock = yf.Ticker(ticker_symbol)
        data = stock.history(interval='1d', start=start_date, end=end_date)
        info = stock.info

        if data.empty:
            st.error(f"🔍 No data found for {ticker_symbol} on the specified dates.")
            return

        with st.expander("🏢 Company Information"):
            st.markdown(f"- **Company:** {info['longName']}")
            st.markdown(f"- **Symbol:** {info['symbol']}")
            st.markdown(f"- **Current Price:** ${info.get('currentPrice', 'N/A'):.2f}")

        if 'officers' in info and info['officers']:
            with st.expander("👥 Key Executives"):
                for i, executive in enumerate(info['officers']):
                    st.markdown(f"- {i+1}. {executive['name']} ({executive['title']}) - Age: {executive.get('age', 'N/A')}, Total Pay: ${executive.get('totalPay', 0):,.2f}")

        with st.expander("💰 Financial Highlights"):
            financial_highlights = {
                "P/E Ratio (Trailing)": info.get('trailingPE', 'N/A'),
                "Forward P/E Ratio": info.get('forwardPE', 'N/A'),
                "Dividend Yield": f"{info.get('dividendYield', 0) * 100:.2f}%" if info.get('dividendYield') is not None else 'N/A',
                "Book Value per Share": f"${info.get('bookValue', 'N/A'):.2f}",
                "Price to Book Ratio": info.get('priceToBook', 'N/A'),
                "Return on Equity": f"{info.get('returnOnEquity', 0) * 100:.2f}%" if info.get('returnOnEquity') is not None else 'N/A'
            }
            for key, value in financial_highlights.items():
                st.markdown(f"- **{key}:** {value}")

        with st.expander("📈 Analyst Recommendations"):
            mean_recommendation = info.get('recommendationKey', 'N/A')
            target_low_price = info.get('targetLowPrice', 'N/A')
            target_high_price = info.get('targetHighPrice', 'N/A')
            st.markdown(f"- **Mean Recommendation:** {mean_recommendation}")
            st.markdown(f"- **Target Price Range:** ${target_low_price:.2f} - ${target_high_price:.2f}")

        with st.expander("ℹ️ Additional Information"):
            additional_info = {
                "Fiscal Year End": unix_timestamp_to_date(info.get('lastFiscalYearEnd')),
                "Shares Outstanding": f"{info.get('sharesOutstanding', 'N/A'):,.0f}",
                "Debt to Equity Ratio": info.get('debtToEquity', 'N/A'),
                "Revenue": f"${info.get('totalRevenue', 'N/A'):,.0f}"
            }
            for key, value in additional_info.items():
                st.markdown(f"- **{key}:** {value}")

        st.markdown("*Please note that this information is for informational purposes only and should not be considered as investment advice.*")
        st.dataframe(data)

    except Exception as e:
        st.error(f"❗ An error occurred: {e}")

# Remember to adjust your Streamlit UI setup accordingly
