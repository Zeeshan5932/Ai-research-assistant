from services.search_service import search_arxiv


def search_arxiv_tool(query: str):
    """Search academic papers on Arxiv and return paper metadata."""
    return search_arxiv(query)


def get_tools():
    return [search_arxiv_tool]