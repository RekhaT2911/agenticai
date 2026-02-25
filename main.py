from fastapi import FastAPI
from pydantic import BaseModel
from router import route_query

app = FastAPI(title="Agentic AI Platform")

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask_agent(request: Query):
    return route_query(request.query)