import requests
from config import BACKEND_URL

def ask_agent(question: str):
    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={"question": question}
    )
    return response.json()
