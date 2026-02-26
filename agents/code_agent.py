from groq import Groq
from agents.base_agent import BaseAgent
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

class CodeAgent(BaseAgent):
    def __init__(self):
        super().__init__("Code Agent")

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

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content