import streamlit as st 
import requests

# Set the app title 
st.title('My First Streamlit App !!') 

# Add a welcome message 
st.write('Welcome to my Streamlit app!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

currency_options = ['USD', 'EUR', 'GBP', 'MYR', 'JPY', 'AUD', 'CAD', 'SGD', 'CNY', 'INR']

# Let user choose the base currency
base_currency = st.selectbox('Select base currency for exchange rates:', currency_options)

# API call using the selected base currency
response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')

if response.status_code == 200:
    data = response.json()
    st.write(f'Exchange rates for base currency: {base_currency}')
    st.json(data)
else:
    st.error(f"API call failed with status code: {response.status_code}")

