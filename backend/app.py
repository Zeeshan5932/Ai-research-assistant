from fastapi import FastAPI
from models.schemas import QueryRequest
from agent.research_agent import get_research_agent

app = FastAPI()
agent = get_research_agent()

@app.post("/ask")
def ask_question(req: QueryRequest):
    result = agent.invoke({"input": req.question})
    return {"answer": result["output"]}
