from fastapi import FastAPI, UploadFile, File
from services.pdf_service import load_pdf
from services.vector_service import create_vector_store
from models.schemas import QueryRequest
from agent.research_agent import get_research_agent
import os
import shutil





app = FastAPI()
agent = get_research_agent()





@app.post("/ask")
def ask_question(req: QueryRequest):
    result = agent.invoke({"input": req.question})
    return {"answer": result["output"]}


@app.post("/upload_pdf")
def upload_pdf(file: UploadFile = File(...)):
    path = f"data/papers/{file.filename}"
    
    
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
        
    docs = load_pdf(path)
    create_vector_store(docs)
    
    return {"message": "PDF uploaded and processed successfully."}
