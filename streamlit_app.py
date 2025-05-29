import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Currency Exchange App", page_icon="💱", layout="centered")

# App title
st.title('💱 Currency Exchange App')
st.markdown("Welcome to the interactive currency exchange app! Choose your currency and see live exchange rates 🌍")

# Currency list sample (abbreviated for brevity; can be expanded)
currency_codes = {
    "United States Dollar (USD)": "USD",
    "Euro (EUR)": "EUR",
    "Japanese Yen (JPY)": "JPY",
    "British Pound (GBP)": "GBP",
    "Malaysian Ringgit (MYR)": "MYR",
    "Singapore Dollar (SGD)": "SGD",
    "Australian Dollar (AUD)": "AUD",
    "Swiss Franc (CHF)": "CHF",
    "Canadian Dollar (CAD)": "CAD",
    "Indian Rupee (INR)": "INR"
}

# Let user select base and target currency
base_currency_name = st.selectbox("Select your base currency:", list(currency_codes.keys()), index=4)
target_currency_name = st.selectbox("Select the target currency to convert to:", list(currency_codes.keys()), index=0)

base_currency = currency_codes[base_currency_name]
target_currency = currency_codes[target_currency_name]

# API Call
response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')

if response.status_code == 200:
    data = response.json()
    rate = data['rates'].get(target_currency)

    if rate:
        st.markdown(f"""
        <div style='background-color:#d1f0d1; padding:20px; border-radius:10px; text-align:center'>
            <h2 style='color:#2e7d32;'>📈 1 {base_currency} = {rate:.4f} {target_currency}</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"Exchange rate not found for {target_currency}.")
else:
    st.error(f"API call failed with status code: {response.status_code}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
