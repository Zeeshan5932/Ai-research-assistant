# 🧠 AI Research Assistant Agent

An **agentic AI research assistant** built with **LangChain**, **FastAPI**, and **Streamlit**. The system can search academic papers, summarize research, and act as an autonomous tool-using agent for students, researchers, and consultants.

---

## 🚀 Features

* 🔍 Search academic papers (Arxiv)
* 🧠 Agent-based reasoning (LangChain)
* 📝 Summarize research papers
* 💬 Conversational memory
* 🌐 FastAPI backend
* 🖥️ Streamlit frontend (chat UI)
* 📚 Extensible to PDF RAG + citations

---

## 🏗️ Project Architecture

```
frontend/
│
├── app.py                # Main Streamlit app
├── api.py                # Backend API calls
# 🧠 AI Research Assistant

An agentic AI research assistant that searches, summarizes, and reasons over academic papers. Built with FastAPI (backend) and Streamlit (frontend), and designed for easy local development and extension (PDF RAG, citation support, vector search).

---

## 🚀 Features

- Search academic papers (ArXiv)
- Agentic reasoning workflows (LangChain)
- Summarize papers and extract key insights
- Conversational memory for multi-turn sessions
- Pluggable vector store for retrieval (FAISS/others)
- Streamlit chat UI and FastAPI backend

---

## 🏗️ Repository layout

```
.
# FastAPI backend, agents, services

├── backend/                
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   └── agent/
│       ├── research_agent.py
│       ├── tools.py
│       ├── memory.py
│       └── prompts.py
├── frontend/               # Streamlit frontend (chat UI)
│   ├── app.py
│   ├── api.py
│   ├── components.py
│   ├── config.py
│   └── requirements.txt
├── models/                 # Pydantic schemas, DTOs
│   └── schemas.py
└── README.md


---

## 🧰 Tech stack

- Python 3.10+
- FastAPI (backend)
- Streamlit (frontend)
- LangChain (agent workflows)
- OpenAI or other LLM providers
- FAISS or other vector stores for retrieval

---

## ⚙️ Quick setup (local)

Prerequisites: Python 3.10+, git, and an OpenAI API key (or another LLM provider key).

1. Clone the repo

```bash
git clone <repo-url>
cd Ai-research-assistant
```

2. Create and activate a virtual environment (recommended)

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install backend dependencies and run the API

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8000
```

The backend will be available at: http://127.0.0.1:8000

4. Install frontend dependencies and run the Streamlit app

```bash
cd ../frontend
pip install -r requirements.txt
python -m streamlit run app.py
```

The frontend will be available at: http://localhost:8501

If you see a launcher error pointing to `Python310`, run Streamlit through the active virtual environment with `python -m streamlit run app.py` instead of the global `streamlit.exe` command.

---

## 🔐 Environment variables

Create a `.env` file in the repository root (or set these in your environment):

```
OPENAI_API_KEY=your_openai_key_here
BACKEND_URL=http://127.0.0.1:8000
```

Adjust other variables in `backend/config.py` or `frontend/config.py` as needed.

---

## 🧪 Usage examples

- Query: "Find recent papers on anomaly detection in finance"
- Request a summary: "Summarize this paper and list limitations"

Use the Streamlit UI for interactive querying, or call the FastAPI endpoints directly for integration.

---

## 🔭 Development notes

- The `backend/agent` module contains agent logic and tools.
- Services implementing search, PDF ingestion, and vector operations live in `backend/services`.
- Add vector data under a `data/` folder if using local persistence.

---

## 📄 License

MIT

---

Built with ❤️ — happy researching!
