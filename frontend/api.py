import requests
from config import BACKEND_URL

# ---------- SEARCH PAPERS ----------
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


# ---------- ASK AGENT (GENERAL / PDF Q&A) ----------
def ask_agent(question):
    payload = {
        "question": question
    }

    res = requests.post(
        f"{BACKEND_URL}/ask",
        json=payload
    )

    if res.status_code != 200:
        return {"error": res.text}

    return res.json()


# ---------- UPLOAD PDF ----------
def upload_pdf(pdf_file):
    files = {"file": pdf_file}

    res = requests.post(
        f"{BACKEND_URL}/upload-pdf",
        files=files
    )

    if res.status_code != 200:
        return {"error": res.text}

    return res.json()


# ---------- COMPARE PAPERS ----------
def compare_papers(papers):
    payload = {
        "papers": papers
    }

    res = requests.post(
        f"{BACKEND_URL}/compare",
        json=payload
    )

    if res.status_code != 200:
        return {"error": res.text}

    return res.json()
