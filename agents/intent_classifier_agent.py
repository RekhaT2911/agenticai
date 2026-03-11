from agents.base_agent import BaseAgent
from intent_classifier import classify_intent


class IntentClassifierAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intent Classifier Agent")

    def handle(self, query: str):
        intent = classify_intent(query)
        return intent