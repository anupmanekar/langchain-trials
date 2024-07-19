import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import os
import camelot
import re

planet_cols = ["Day", "Sid T", "Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "True Rahu", "Mean Rahu", "Lilith", "Chiron"]
sign_alpha_mapping = {"a": "Aries", "b": "Taurus", "c": "Gemini", "d": "Cancer", "e": "Leo", "f": "Virgo", "g": "Libra", "h": "Scorpio", 
                      "i" : "Saggi", "j": "Capri", "k": "Aqua", "l": "Pisces"}
tables = camelot.read_pdf('../resources/lahiri_jan_1800.pdf', pages="2", flavor="stream")
monthly_map = {}


st.write(tables[0].df)

""" mongo_pass = os.environ["MONGODB_ATLAS_KEY"]
uri = "mongodb+srv://manekaranup:" + mongo_pass + "@cluster0.tgijnsz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    "Pinged your deployment. You successfully connected to MongoDB!"
    db_name = client.get_database("astro_ai")
    nifty_indexes = db_name.get_collection("lahiri_ayanamsa")
    "Total Documents are:" + str(nifty_indexes.count_documents(filter={}))
except Exception as e:
    e """