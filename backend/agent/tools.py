def get_tools():
    from langchain.tools import Tool
    from services.search_service import search_arxiv

    return [
        Tool(
            name="search_arxiv",
            func=search_arxiv,
            description=(
                "Search academic papers on Arxiv. "
                "Use this when the user asks for research papers, literature reviews, or recent studies. "
                "Return paper title, authors, year, summary, and PDF link."
            ),
        )
    ]