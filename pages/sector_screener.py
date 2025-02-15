import streamlit as st
import pandas as pd


# Apply the same theme as the main page
st.markdown(
    """
    <style>
        /* General Page Styling */
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Inter', sans-serif;
        }
        .stApp {
            background-color: #000;
        }
        /* Titles & Subtitles */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #fff;
            text-align: center;
            margin-top: 20px;
        }
        .subtitle {
            font-size: 18px;
            color: #fff;
            text-align: center;
        }
        /* Sidebar */
        .stSidebar {
            background-color: #111 !important;
            color: #fff;
        }
        /* Data Tables */
        .stDataFrame {
            color: #000;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Load the dataset (ensure the file is uploaded on Streamlit)
def load_data():
    df = pd.read_excel("pages/DATASET.xlsx")
    df.columns = df.columns.str.strip()  # Strip extra spaces from column names
    return df

# Function to filter the data based on selected filters
def filter_data(df, company_name, sector, symbol, supplier_company, customer_company, sub_sector):
    filtered_df = df
    
    if company_name:
        filtered_df = filtered_df[filtered_df['COMPANY NAME'].str.contains(company_name, case=False, na=False)]
    if sector:
        filtered_df = filtered_df[filtered_df['SECTOR'].str.contains(sector, case=False, na=False)]
    if sub_sector:
        filtered_df = filtered_df[filtered_df['SUBSECTOR'].str.contains(sector, case=False, na=False)]
    if symbol:
        filtered_df = filtered_df[filtered_df['SYMBOL'].str.contains(symbol, case=False, na=False)]
    if supplier_company:
        filtered_df = filtered_df[filtered_df['SUPPLIER COMPANY'].str.contains(supplier_company, case=False, na=False)]
    if customer_company:
        filtered_df = filtered_df[filtered_df['CUSTOMER COMPANY'].str.contains(customer_company, case=False, na=False)]
    
    return filtered_df

# Function to count supplier occurrences for the selected sector
def supplier_occurrence_by_sector(df, selected_sector):
    sector_df = df[df['SECTOR'].str.contains(selected_sector, case=False, na=False)]
    supplier_count = sector_df['SUPPLIER COMPANY'].value_counts().reset_index()
    supplier_count.columns = ['SUPPLIER COMPANY', 'Occurrences']
    
    return supplier_count

# Streamlit app UI
def main():
    st.title("Sector Screener")

    # Load the data
    df = load_data()

    # Sidebar filters
    st.sidebar.header("Filters")
    
    company_name = st.sidebar.selectbox("Select Company Name", [""] + list(df['COMPANY NAME'].unique()))
    sector = st.sidebar.selectbox("Select Sector", [""] + list(df['SECTOR'].unique()))
    sub_sector = st.sidebar.selectbox("Select Sub Sector", [""] + list(df['SUB SECTOR'].unique()))
    symbol = st.sidebar.selectbox("Select Symbol", [""] + list(df['SYMBOL'].unique()))
    supplier_company = st.sidebar.selectbox("Select Supplier's Company", [""] + list(df['SUPPLIER COMPANY'].unique()))
    customer_company = st.sidebar.selectbox("Select Customer's Company", [""] + list(df['CUSTOMER COMPANY'].unique()))

    # Filter the data based on inputs
    filtered_df = filter_data(df, company_name, sector, symbol, supplier_company, customer_company, sub_sector)

    # Sector selection for supplier occurrence table
    selected_sector = st.sidebar.selectbox("Select Sector for Occurrence", filtered_df['SECTOR'].unique())
    
    # Get supplier occurrences for the selected sector from filtered data
    supplier_count = supplier_occurrence_by_sector(filtered_df, selected_sector)

    # Display the filtered data
    st.subheader("Filtered Data")
    if not filtered_df.empty:
        st.dataframe(filtered_df)
    else:
        st.write("No data available with the selected filters.")

    # Display the supplier occurrences by sector
    st.subheader(f"Supplier Occurrences in {selected_sector} Sector")
    if not supplier_count.empty:
        st.dataframe(supplier_count)
    else:
        st.write("No suppliers found for the selected sector.")

if __name__ == "__main__":
    main()
