from groq import Groq
from agents.base_agent import BaseAgent
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

class DynamicAgent(BaseAgent):
    def __init__(self):
        super().__init__("Dynamic Agent")

    def handle(self, query: str):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Format responses clearly like ChatGPT."},
                {"role": "user", "content": query}
            ]
        )

        return response.choices[0].message.content