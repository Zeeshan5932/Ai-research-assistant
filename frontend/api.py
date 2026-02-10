import requests
from config import BACKEND_URL

def search_papers(query, from_year, to_year):
    return requests.post(
        f"{BACKEND_URL}/search",
        json={
            "query": query,
            "from_year": from_year,
            "to_year": to_year
        }
    ).json()

def ask_agent(question):
    return requests.post(
        f"{BACKEND_URL}/ask",
        json={"question": question}
    ).json()

def upload_pdf(pdf_file):
    files = {"file": pdf_file}
    return requests.post(
        f"{BACKEND_URL}/upload-pdf",
        files=files
    ).json()

def compare_papers(papers):
    return requests.post(
        f"{BACKEND_URL}/compare",
        json={"papers": papers}
    ).json()
