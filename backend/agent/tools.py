# from langchain.tools import Tool
# from services.search_service import search_arxiv

# def get_tools():
#     return [
#         Tool(
#             name="search_arxiv",
#             func=search_arxiv,
#             description=(
#                 "Search academic papers on Arxiv. "
#                 "Use this for research, literature review, and recent papers."
#             )
#         )
#     ]


from langchain.tools import Tool
from services.search_service import search_arxiv
from services.vector_service import load_vector_store


def pdf_qa_tool(query: str):
    db = load_vector_store()
    results = db.similarity_search(query, k=5)
    return "\n" .join([d.page_content for d in results])


def get_tool():
    return [
        Tool(
            name="search_arxiv",
            func=search_arxiv,
            description=(
                "Search academic papers on Arxiv. "
                "Use this for research, literature review, and recent papers."
            )
        ),
        Tool(
            name="pdf_qa",
            func=pdf_qa_tool,
            description=(
                "Query PDFs in the vector store. "
                "Use this for answering questions about specific PDFs."
            )
        )
    ]