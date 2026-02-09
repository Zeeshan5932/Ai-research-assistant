from fastapi import FastAPI
from models.schemas import QueryRequest
from agent.research_agent import get_research_agent_response


app = FastAPI()

@app.post("/ask")

def ask_question(req: QueryRequest):
    response = get_research_agent_response(req.question)
    return {"answer": response}