def format_citation(paper):
    authors = ", ".join(paper["authors"])
    return f"{authors} ({paper['year']}) - {paper['title']}"
