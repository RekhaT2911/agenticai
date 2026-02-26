import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_secret(key):
    return os.getenv(key) or st.secrets.get(key)

OPENWEATHER_API_KEY = get_secret("OPENWEATHER_API_KEY")
RAPID_API_KEY = get_secret("RAPID_API_KEY")
ADZUNA_APP_ID = get_secret("ADZUNA_APP_ID")
ADZUNA_APP_KEY = get_secret("ADZUNA_APP_KEY")
GROQ_API_KEY = get_secret("GROQ_API_KEY")