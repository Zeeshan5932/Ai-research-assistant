import streamlit as st

# ---------- CHAT MESSAGES ----------
def user_message(msg):
    st.markdown(
        f"""
        <div style="background-color:#e8f0fe; padding:10px; border-radius:8px; margin-bottom:8px;">
        🧑 <b>You:</b> {msg}
        </div>
        """,
        unsafe_allow_html=True
    )

def agent_message(msg):
    st.markdown(
        f"""
        <div style="background-color:#f1f3f4; padding:10px; border-radius:8px; margin-bottom:8px;">
        🤖 <b>Agent:</b> {msg}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- PAPER CARD ----------
def paper_card(paper, index=None):
    title_prefix = f"{index}. " if index else ""
    st.markdown(
        f"""
        <div style="border:1px solid #ddd; padding:12px; border-radius:8px; margin-bottom:12px;">
        <b>{title_prefix}{paper['title']}</b><br>
        <i>{', '.join(paper['authors'])}</i> ({paper['year']})<br><br>
        {paper['summary'][:300]}...
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- SECTION HEADER ----------
def section_header(title, icon=""):
    st.markdown(f"## {icon} {title}")
