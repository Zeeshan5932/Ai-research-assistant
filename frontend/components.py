import streamlit as st

def user_message(msg):
    st.markdown(f"🧑 **You:** {msg}")

def agent_message(msg):
    st.markdown(f"🤖 **Agent:** {msg}")
