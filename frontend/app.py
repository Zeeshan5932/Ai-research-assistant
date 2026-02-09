import streamlit as st
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
    response = ask_agent(question)
    st.session_state.chat.append(("agent", response["answer"]))

st.divider()

for role, msg in st.session_state.chat:
    if role == "user":
        user_message(msg)
    else:
        agent_message(msg)
