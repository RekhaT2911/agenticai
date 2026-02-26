from groq import Groq
from agents.base_agent import BaseAgent
import streamlit as st
import os


class CodeAgent(BaseAgent):
    def __init__(self):
        super().__init__("Code Agent")

        # Read API key directly from Streamlit secrets or environment
        api_key = None

        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
        else:
            api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in Streamlit Secrets")

        self.client = Groq(api_key=api_key)

    def handle(self, query: str):

        prompt = f"""
        You are a professional software engineer.

        Provide:
        1. Basic implementation
        2. Optimized version
        3. Time complexity
        4. Short explanation

        Format cleanly with headings.

        Question: {query}
        """

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content