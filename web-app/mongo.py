
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import os

mongo_pass = os.environ["MONGODB_ATLAS_KEY"]
uri = "mongodb+srv://manekaranup:" + mongo_pass + "@cluster0.tgijnsz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    "Pinged your deployment. You successfully connected to MongoDB!"
    db_name = client.get_database("nifty_data")
    nifty_indexes = db_name.get_collection("nifty_indexes")
    "Total Documents are:" + str(nifty_indexes.count_documents(filter={}))
except Exception as e:
    e

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    dataframe = pd.read_csv(uploaded_file)
    dataframe['Date'] = pd.to_datetime(dataframe['Date']).dt.tz_localize('UTC')
    st.write(dataframe)
    #data = dataframe.to_dict(orient='records')
    #nifty_indexes.insert_many(data)
    "Total Documents are:" + str(nifty_indexes.count_documents(filter={}))