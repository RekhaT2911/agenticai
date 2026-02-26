import os
import streamlit as st

def get_secret(key):
    # First check Streamlit secrets
    if key in st.secrets:
        return st.secrets[key]
    # Then check environment variables (local .env)
    return os.getenv(key)

OPENWEATHER_API_KEY = get_secret("OPENWEATHER_API_KEY")
RAPID_API_KEY = get_secret("RAPID_API_KEY")
ADZUNA_APP_ID = get_secret("ADZUNA_APP_ID")
ADZUNA_APP_KEY = get_secret("ADZUNA_APP_KEY")
GROQ_API_KEY = get_secret("GROQ_API_KEY")