"""
Day 13: Agent Serving with FastAPI
Concept: Wrapping our LangGraph agent in a production-ready REST API using FastAPI.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agentic AI API")

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_agent(request: QueryRequest):
    # Simulate agent invocation
    return {"response": f"Agent processed: {request.query}"}

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    print("FastAPI Agent Server ready for deployment.")
