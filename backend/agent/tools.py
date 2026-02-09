from langchain.tools import Tool
from services.search_service import search_arxiv

def get_tools():
    return [
        Tool(
            name="search_arxiv",
            func=search_arxiv,
            description=(
                "Search academic papers on Arxiv. "
                "Use this for research, literature review, and recent papers."
            )
        )
    ]
