from groq import Groq
from agents.base_agent import BaseAgent
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

class HealthAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Agent")

    def handle(self, query: str):

        prompt = f"""
        Provide general health advice.
        Do NOT provide medical diagnosis.
        Format neatly with bullet points.

        User Query: {query}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content