import requests
from config import BACKEND_URL

def ask_agent(question: str):
    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={"question": question},
        timeout=60,
    )

    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        detail = response.text.strip() or str(exc)
        return {"answer": f"Backend error ({response.status_code}): {detail}"}

    try:
        return response.json()
    except ValueError:
        return {"answer": response.text.strip() or "Backend returned an empty response."}
