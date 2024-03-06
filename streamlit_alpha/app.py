import streamlit as st
from pages import home, stock_data, stock_statistics

PAGES = {
    "Home": home,
    "Stock Data": stock_data,
    "Stock Statistics": stock_statistics
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
