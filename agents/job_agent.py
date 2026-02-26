import requests
from agents.base_agent import BaseAgent

class JobAgent(BaseAgent):
    def __init__(self):
        super().__init__("Job Agent")

    def handle(self, query: str):

        response = requests.get("https://remotive.com/api/remote-jobs")
        data = response.json()

        jobs = data.get("jobs", [])[:5]

        if not jobs:
            return "💼 No jobs found at the moment."

        formatted = "💼 **Latest Remote Jobs**\n\n"

        for i, job in enumerate(jobs, 1):
            formatted += f"{i}. {job['title']}\n"
            formatted += f"   🏢 {job['company_name']}\n"
            formatted += f"   🔗 {job['url']}\n\n"

        return formatted