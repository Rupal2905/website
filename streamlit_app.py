import streamlit as st

def main():
    # Page Configuration
    st.set_page_config(page_title="Stock Insights", layout="wide")

    # Custom CSS for Modern Theme
    st.markdown(
        """
        <style>
            /* General Page Styling */
            body {
                background-color: #000;
                color: white;
                font-family: 'Inter', sans-serif;
            }
            .stApp {
                background-color: #000;
            }

            /* Navigation Bar */
            .nav-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 60px;
                background-color: black;
                position: relative;
                width: 100%;
                top: 20px;
                left: 0;
                z-index: 1000;
            }
            .nav-links {
                display: flex;
                gap: 20px;
            }
            .nav-links a {
                color: white;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
                transition: color 0.3s;
            }
            .nav-links a:hover {
                color: #d4af37;
            }
            .nav-brand {
                font-size: 20px;
                font-weight: bold;
                color: white;
            }

            /* Hero Section */
            .hero-section {
                text-align: center;
                margin-top: 150px;
            }
            .hero-title {
                font-size: 60px;
                font-weight: bold;
                margin-bottom: 10px;
                color: white;
            }
            .hero-subtitle {
                font-size: 18px;
                color: #aaa;
            }

            /* Stock Screener Card */
            .card-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 100px auto;
                max-width: 1200px;
                padding: 40px;
                background: transparent;
                border-radius: 15px;
            }
            .card-text {
                flex: 1;
                padding-right: 40px;
                padding-left: 100px;
                color: #fff;
            }
            .card-text h2 {
                font-size: 40px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .card-text p {
                font-size: 18px;
                color: #ddd;
                margin-bottom: 20px;
            }
            .card-button {
                padding: 12px 30px;
                background: #2c0051;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 30px;
                cursor: pointer;
                transition: background 0.3s;
                text-decoration: none;
                display: inline-block;
            }

     
 
            .card-button:hover {
                background: #5a009a;
            }
            .card-image img {
                width: 100%;
                max-width: 500px;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Navigation Bar
    st.markdown(
        """
        <div class="nav-container">
            <div class="nav-brand">Stock Insights</div>
            <div class="nav-links">
                <a href="#">Dashboard</a>
                <a href="#">Analytics</a>
                <a href="#">Strategies</a>
                <a href="#">News</a>
            </div>
            <a href="#" class="get-started-btn">Get Started</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Hero Section
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-title">Your Complete NSE Stocks<br>Analysis Dashboard</div>
            <div class="hero-subtitle">
                Access comprehensive stock data with detailed insights and interactive analysis tools for all NSE-listed stocks.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Stock Screener Card
    st.markdown(
        """
        <div class="card-container">
            <div class="card-text">
                <h2>Stock Screener for Smart Investing</h2>
                <p>Filter and analyze stocks with advanced screening tools to make informed investment decisions.</p>
                <a href="pages/sector_screener.py" class="card-button" style="text-decoration: none; color: white; display: inline-block; text-align: center;">
                Stock Screener
                </a>
        </div>
            <div class="card-image">
                <img src="https://th.bing.com/th/id/R.53485e05be08d65150344fd995da6565?rik=THoUVu53lCt9Eg&riu=http%3a%2f%2fwww.learnattic.com%2fwp-content%2fuploads%2f2020%2f07%2fdata-analysis.jpg&ehk=S7WlnPwoJ33bhV%2fM5rpP1BQBlzuYlNZff2UjDCwtHio%3d&risl=&pid=ImgRaw&r=0" alt="Stock Market Image">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Gann Dates Card
    st.markdown(
        """
        <div class="card-container">
            <div class="card-image">
                <img src="https://2.bp.blogspot.com/-7Tb71YSf60M/VlSLlgB-AoI/AAAAAAAACKw/3vidmScXK4I/w1200-h630-p-k-no-nu/DAX%2Bindex%2BWD%2BGANN%2Banalysis-24-nov.jpg" alt="Gann Dates Image">
            </div>
            <div class="card-text">
                <h2>Gann Dates and Market Cycles</h2>
                <p>Discover important Gann dates to anticipate market trends and make strategic trading decisions.</p>
                <a href="pages/gann_dates.py" class="card-button" style="text-decoration: none; color: white; display: inline-block; text-align: center;">Explore Gann Dates</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card-container">
            <div class="card-text">
                <h2>Top Stock Related News </h2>
                <p>Get insights of comapnies next move to plan your investing </p>
                <a href="pages/sector_screener.py" class="card-button" style="text-decoration: none; color: white; display: inline-block; text-align: center;">Stock Screener</a>
            </div>
            <div class="card-image">
                <img src="https://d.newsweek.com/en/full/2383613/newsweek-stock-market-today.png", alt="stock news iamge">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
