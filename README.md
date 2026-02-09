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
ai-research-assistant/
│
├── backend/              # FastAPI + LangChain agent
│├── frontend/            # Streamlit app
│├── data/                # PDFs & vector store
│├── README.md
│└── .env
```

---

## 🧠 Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* OpenAI / LLMs
* FAISS (Vector DB)

### Frontend

* Streamlit

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <repo-url>
cd ai-research-assistant
```

---

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup (Streamlit)

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Frontend will run at:

```
http://localhost:8501
```

---

## 🔐 Environment Variables

Create a `.env` file in root directory:

```env
OPENAI_API_KEY=your_openai_key_here
```

---

## 🧪 Example Usage

Ask the assistant:

* "Find recent papers on anomaly detection in finance"
* "Summarize the latest research on fraud detection"

---

## 📌 Future Enhancements

* 📄 PDF upload + RAG Q&A
* 📊 Compare multiple papers
* 📚 APA / IEEE citations
* ☁️ Deployment (AWS / Azure)

---

## 🎓 Ideal For

* Final Year Projects (FYP)
* Research assistants
* Consultants
* AI portfolio projects

---

## 🏆 License

MIT License

---

**Built with ❤️ using Agentic AI**
