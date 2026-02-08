import arxiv

def search_arxiv(query: str, max_results: int = 5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []
    for paper in search.results():
        results.append({
            "title": paper.title,
            "authors": [a.name for a in paper.authors],
            "summary": paper.summary,
            "pdf_url": paper.pdf_url,
            "year": paper.published.year
        })

    return results
