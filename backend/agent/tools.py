from langchain.tools import Tool
from services.search_service import search_arxiv

def get_tools():
    return [
        Tool(
            name="Search Arxiv",
            func=lambda q: search_arxiv(q),
            description="Search academic papers on Arxiv"
        )
    ]
