def get_tools():
    from services.search_service import search_arxiv

    return [search_arxiv]