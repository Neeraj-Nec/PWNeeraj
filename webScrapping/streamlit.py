import streamlit as st
import pandas as pd
from web_scrapping import f_main  # Assuming you have a web_scrapping module with a main function

# Function to fetch data based on user input URL
def fetch_data(url):
    data = f_main(url)
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    # Set title for the app
    st.title("Flipkart Scraper App")

    # User input for Flipkart URL
    url = st.text_input("Enter Flipkart URL:")
    
    if st.button("Ok"):
        # Fetching data and displaying table with images
        df = fetch_data(url)
        st.write(f"Table for {url}")
        for index, row in df.iterrows():
            st.write(f"Name: {row['name']}, Rating: {row['rating']}")
            st.image(row['image'], width=100)

if __name__ == "__main__":
    main()

