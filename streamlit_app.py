import streamlit as st 
import requests

# Set the app title 
st.title('My First Streamlit App !!') 

# Add a welcome message 
st.write('Welcome to my Streamlit app!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Set the app title
st.title('Currency Exchange Rate Viewer 💱')

# Add a welcome message
st.write('Welcome to the Currency Exchange app!')

# Create a text input for a custom message
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Currency options (you can expand this list)
currency_options = [
    'USD', 'EUR', 'GBP', 'MYR', 'JPY', 'AUD', 'CAD', 'SGD', 'CNY', 'INR'
]

# Let user choose the base currency
base_currency = st.selectbox('Select base currency:', currency_options)

# API call using the selected base currency
api_url = f'https://api.vatcomply.com/rates?base={base_currency}'
response = requests.get(api_url)

# Display the response
if response.status_code == 200:
    data = response.json()
    st.write(f'Exchange rates for base currency: {base_currency}')
    st.json(data)  # nicely formatted JSON output
else:
    st.error(f"API call failed with status code: {response.status_code}")



