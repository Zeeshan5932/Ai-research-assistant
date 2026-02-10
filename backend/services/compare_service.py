def compare_papers(papers: list):
    comparison = []

    for paper in papers:
        comparison.append(
            f"""
Title: {paper['title']}
Year: {paper['year']}
Method Summary: {paper['summary'][:300]}...
"""
        )

    return "\n---\n".join(comparison)
