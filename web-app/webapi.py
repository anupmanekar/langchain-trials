from io import StringIO
import requests
import os
import pandas as pd
import streamlit as st

advantage_api_key = os.environ["ADVANTAGE_API_KEY"]

st.write("Fetching CSV data from API")
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SBIN.BSE&datatype=csv&apikey=' + advantage_api_key
r = requests.get(url)
csv_data = r.text
df = pd.read_csv(StringIO(csv_data))
df

st.write("Fetching JSON data from API")
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SBIN.BSE&datatype=json&apikey=' + advantage_api_key
r = requests.get(url)
json_data = r.json()
df = pd.read_json(json_data)
df