import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

# Define your holidays and functions as they are in your code
nse_holidays = [
    "22-01-2024", "26-01-2024", "08-03-2024", "25-03-2024", "29-03-2024", "11-04-2024",
    "17-04-2024", "01-05-2024", "20-05-2024", "17-06-2024", "17-07-2024", "15-08-2024",
    "02-10-2024", "01-11-2024", "15-11-2024", "25-12-2024",
]

nse_holidays = [datetime.strptime(date, "%d-%m-%Y") for date in nse_holidays]

def is_trading_holiday(date):
    if date.weekday() in [5, 6]:  
        return True
    if date in nse_holidays:
        return True
    return False

def calculate_future_dates(start_date, cycle=1):
    degrees = [30, 45, 60, 72, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
    factor = 1.0146 
    future_dates = {}

    if cycle == 1:
        for degree in degrees:
            days_to_add = degree * factor
            future_date = start_date + timedelta(days=days_to_add)
            
            while is_trading_holiday(future_date):
                future_date += timedelta(days=1)  
            
            future_dates[degree] = future_date 
        
        if 360 not in future_dates:
            raise ValueError("360-degree date from the first cycle is not available.")
        return future_dates 

    if cycle == 2:
        last_360_degree_date = start_date  
        
        for degree in degrees:
            days_to_add = degree * factor
            future_date = last_360_degree_date + timedelta(days=days_to_add)
            
            while is_trading_holiday(future_date):
                future_date += timedelta(days=1)  
            
            future_dates[f"Degree_{degree}_Second_Cycle_Date"] = future_date

    return future_dates

# Load your Excel data (adjust this path based on your system)
df = pd.read_excel('pages/SWING HIGH.xlsx')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')

date_to_scripts = {}

# Calculate future dates for all scripts in the DataFrame
for index, row in df.iterrows():
    start_date = row['Date'] 
    future_dates = calculate_future_dates(start_date, cycle=1) 
    
    for degree, date in future_dates.items():
        if isinstance(degree, int) and degree <= 360:  
            date_str = date.strftime("%d-%m-%Y")
            df.loc[index, f'Degree_{degree}_Date'] = date_str
            
            if date_str not in date_to_scripts:
                date_to_scripts[date_str] = []
            date_to_scripts[date_str].append((row['Script'], degree))

    last_360_degree_date = future_dates.get(360)  
    
    if last_360_degree_date:
        future_dates_second_cycle = calculate_future_dates(last_360_degree_date, cycle=2)  # Second cycle

        for degree, date in future_dates_second_cycle.items():
            if isinstance(degree, str) and degree.startswith("Degree_"):  
                degree_in_second_cycle = degree
                date_str = date.strftime("%d-%m-%Y")
                df.loc[index, degree_in_second_cycle] = date_str
                
                if date_str not in date_to_scripts:
                    date_to_scripts[date_str] = []
                date_to_scripts[date_str].append((row['Script'], degree_in_second_cycle))

# Define the Streamlit app
def user_interaction():
    st.title('Script and Degree Finder')

    filter_choice = st.radio("Do you want to filter by:", ("Date", "Script"))

    if filter_choice == "Date":
        date_input = st.text_input("Enter the date (dd-mm-yyyy):")
        if date_input:
            try:
                query_date = datetime.strptime(date_input, "%d-%m-%Y")
                scripts_and_degrees = get_scripts_for_date(query_date)

                if scripts_and_degrees:
                    st.write(f"Scripts and degrees on {query_date.strftime('%d-%m-%Y')}:")
                    for script, degree in scripts_and_degrees:
                        st.write(f"Script: {script}, Degree: {degree}")
                else:
                    st.write(f"No scripts found for {query_date.strftime('%d-%m-%Y')}.")
            except ValueError:
                st.write("Invalid date format. Please use dd-mm-yyyy.")

    elif filter_choice == "Script":
        script_input = st.text_input("Enter the script name:")
        if script_input:
            script_found = False
            script_degrees = []
            
            for date_str, scripts_degrees in date_to_scripts.items():
                for script, degree in scripts_degrees:
                    if script.lower() == script_input.lower():
                        script_degrees.append((date_str, degree))
                        script_found = True

            if script_found:
                st.write(f"Dates and degrees for script '{script_input}':")
                for degree_column in date_to_scripts:
                    for degree_date in script_degrees:
                        st.write(f"{degree_column}: {degree_date[0]}")
            else:
                st.write(f"No data found for script '{script_input}'.")

def get_scripts_for_date(query_date):
    query_date_str = query_date.strftime("%d-%m-%Y") 
    if query_date_str in date_to_scripts:
        return date_to_scripts[query_date_str]
    else:
        return []

# Run the user interaction function
user_interaction()
