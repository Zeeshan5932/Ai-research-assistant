import streamlit as st
import requests
from api import ask_agent
from components import user_message, agent_message

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Research Assistant")
st.caption("Agentic AI for research, papers, and literature review")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Ask a research question:")

if st.button("Ask") and question:
    st.session_state.chat.append(("user", question))
    try:
        response = ask_agent(question)
        st.session_state.chat.append(("agent", response.get("answer", "No answer returned.")))
    except requests.RequestException as exc:
        st.session_state.chat.append(("agent", f"Request failed: {exc}"))
    except Exception as exc:
        st.session_state.chat.append(("agent", f"Unexpected error: {exc}"))

st.divider()

for role, msg in st.session_state.chat:
    if role == "user":
        user_message(msg)
    else:
        agent_message(msg)
