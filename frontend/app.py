# import streamlit as st
# from api import ask_agent
# from components import user_message, agent_message

# st.set_page_config(
#     page_title="AI Research Assistant",
#     page_icon="📚",
#     layout="centered"
# )

# st.title("📚 AI Research Assistant")
# st.caption("Agentic AI for research, papers, and literature review")

# if "chat" not in st.session_state:
#     st.session_state.chat = []

# question = st.text_input("Ask a research question:")

# if st.button("Ask") and question:
#     st.session_state.chat.append(("user", question))
#     response = ask_agent(question)
#     st.session_state.chat.append(("agent", response["answer"]))

# st.divider()

# for role, msg in st.session_state.chat:
#     if role == "user":
#         user_message(msg)
#     else:
#         agent_message(msg)



import streamlit as st
from api import search_papers, ask_agent, upload_pdf, compare_papers
from components import (
    user_message,
    agent_message,
    paper_card,
    section_header
)

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Assistant")
st.caption("Search • Read PDFs • Compare Research Papers")

# Session state
if "papers" not in st.session_state:
    st.session_state.papers = []

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(
    ["🔍 Search Papers", "📄 PDF Q&A", "⚖️ Compare Papers"]
)

# ---------- TAB 1: SEARCH ----------
with tab1:
    section_header("Search Research Papers", "🔍")

    query = st.text_input("Research question")
    col1, col2 = st.columns(2)

    with col1:
        from_year = st.number_input("From year", 2000, 2025, 2020)
    with col2:
        to_year = st.number_input("To year", 2000, 2025, 2024)

    if st.button("Search Papers"):
        result = search_papers(query, from_year, to_year)
        papers = result.get("papers") if isinstance(result, dict) else None
        if not papers:
            st.error(result.get("error", "No papers returned from search."))
            st.session_state.papers = []
        else:
            st.session_state.papers = papers

    if st.session_state.papers:
        st.success(f"Found {len(st.session_state.papers)} papers")
        for i, paper in enumerate(st.session_state.papers, 1):
            paper_card(paper, i)

# ---------- TAB 2: PDF Q&A ----------
with tab2:
    section_header("Ask Questions from PDF", "📄")

    pdf = st.file_uploader("Upload research PDF", type="pdf")

    if pdf:
        res = upload_pdf(pdf)
        st.success(res["message"])

    question = st.text_input("Ask a question from the uploaded PDF")

    if st.button("Ask PDF"):
        if question:
            res = ask_agent(question)
            agent_message(res["answer"])

# ---------- TAB 3: COMPARE ----------
with tab3:
    section_header("Compare Research Papers", "⚖️")

    if not st.session_state.papers:
        st.info("Please search papers first (Tab 1)")
    else:
        titles = [p["title"] for p in st.session_state.papers]
        selected = st.multiselect("Select papers", titles)

        if st.button("Compare Selected Papers"):
            selected_papers = [
                p for p in st.session_state.papers
                if p["title"] in selected
            ]

            if len(selected_papers) < 2:
                st.warning("Select at least 2 papers")
            else:
                res = compare_papers(selected_papers)
                agent_message(res["comparison"])
