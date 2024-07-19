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
tables = camelot.read_pdf('../resources/slae_2000.pdf', pages="2", flavor="stream", table_areas=['52,763,547,440','52,394,547,94'])
monthly_map = {}

for table in tables:
    my_df = table.df
    month_year_key = my_df[0][0]
    my_df = my_df[2:]
    my_df.columns = planet_cols
    for planet in planet_cols:
        sign_found = ""
        for index, row in my_df.iterrows():
            if (planet != "Day" and planet != "Sid T"):
                if re.search(r'[a-l]', row[planet]):
                    sign_found = re.search(r'[a-l]', row[planet])
                    row[planet] = row[planet].translate(str.maketrans(sign_alpha_mapping))
                else:
                    if (sign_found != ""):
                        row[planet] = row[planet].replace("°", "°" + sign_alpha_mapping[sign_found.group(0)])
                    else:
                        row[planet] = row[planet]

    monthly_map[month_year_key] = my_df


st.write(monthly_map["JANUARY 2000"])

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