from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str

# class SearchRequest(BaseModel):
#     title: str
#     authors: list
#     summary: str
#     pdf_url: str
#     year: int