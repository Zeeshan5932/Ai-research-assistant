# from fastapi import FastAPI, UploadFile, File
# from services.pdf_service import load_pdf
# from services.vector_service import create_vector_store
# from models.schemas import QueryRequest, SearchRequest
# from services.search_service import search_arxiv
# from agent.research_agent import get_research_agent
# import os
# import shutil





# app = FastAPI()
# agent = get_research_agent()





# @app.post("/ask")
# def ask_question(req: QueryRequest):
#     # langgraph agents use .invoke() instead of .run()
#     result = agent.invoke({"messages": [("user", req.question)]})
#     # Extract the final message from the result
#     if result and "messages" in result:
#         final_message = result["messages"][-1]
#         return {"answer": final_message.content if hasattr(final_message, 'content') else str(final_message)}
#     return {"answer": str(result)}


# @app.post("/upload_pdf")
# def upload_pdf(file: UploadFile = File(...)):
#     path = f"data/papers/{file.filename}"
    
    
#     with open(path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
        
        
#     docs = load_pdf(path)
#     create_vector_store(docs)
    
#     return {"message": "PDF uploaded and processed successfully."}


# @app.post("/search")

# def search_papers(req: SearchRequest):
#     papers = search_arxiv(
#         query=req.query,
#         from_year=req.from_year,
#         to_year=req.to_year
#     )
#     return {"papers": papers}


from fastapi import FastAPI
from .models.schemas import QueryRequest
from .agent.research_agent import get_research_agent

app = FastAPI()
agent = get_research_agent()

@app.post("/ask")
def ask_question(req: QueryRequest):
    response = agent.invoke({"input": req.question})
    return {"answer": response["output"]}

