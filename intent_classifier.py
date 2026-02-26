def classify_intent(query: str):
    query = query.lower()

    if "weather" in query:
        return "weather"
    elif "train" in query or "ticket" in query:
        return "booking"
    elif "optimize" in query or "debug" in query or "code" in query:
        return "code"
    elif "health" in query or "symptom" in query:
        return "health"
    elif "job" in query or "resume" in query or "education" in query:
        return "job"
    else:
        return "dynamic"