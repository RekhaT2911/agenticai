from intent_classifier import classify_intent
from agents.weather_agent import WeatherAgent
from agents.booking_agent import BookingAgent
from agents.code_agent import CodeAgent
from agents.health_agent import HealthAgent
from agents.job_agent import JobAgent
from agents.dynamic_agent import DynamicAgent

def route_query(query: str):

    intent = classify_intent(query)

    agents = {
        "weather": WeatherAgent(),
        "booking": BookingAgent(),
        "code": CodeAgent(),
        "health": HealthAgent(),
        "job": JobAgent(),
        "dynamic": DynamicAgent()
    }

    return agents[intent].handle(query)