from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str

class SearchResult(BaseModel):
    title: str
    authors: list
    summary: str
    pdf_url: str
    year: int