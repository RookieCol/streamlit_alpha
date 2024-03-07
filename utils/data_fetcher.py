# import yfinance as yf

# def fetch_stock_data(ticker_symbol, time_frame):
#     """
#     Fetches stock data for the specified ticker symbol and time frame.

#     Parameters:
#         ticker_symbol (str): The ticker symbol of the stock.
#         time_frame (str): The time frame for the data (e.g., '1d' for 1 day, '1wk' for 1 week, '1mo' for 1 month).

#     Returns:
#         pandas.DataFrame or None: DataFrame containing the stock data if successful, None otherwise.
#     """
#     try:
#         # Fetch stock data using yfinance
#         stock_data = yf.ticker(ticker_symbol, period=time_frame)

#         # If data is fetched successfully, return it
#         return stock_data
#     except Exception as e:
#         # If there's an error fetching data, print the error and return None
#         print(f"Error fetching data for {ticker_symbol}: {str(e)}")
#         return None
