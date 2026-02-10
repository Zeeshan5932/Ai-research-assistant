import requests
from config import BACKEND_URL

def search_papers(query, from_year, to_year):
    payload = {
        "query": query,
        "from_year": int(from_year),
        "to_year": int(to_year)
    }

    res = requests.post(
        f"{BACKEND_URL}/search",
        json=payload
    )

    if res.status_code != 200:
        return {"error": res.text}

    return res.json()


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
