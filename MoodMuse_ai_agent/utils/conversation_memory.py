# utils/conversation_memory.py
import streamlit as st

def initialize_chat():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_to_chat(user_msg, ai_response):
    st.session_state.chat_history.append({"user": user_msg, "ai": ai_response})

def get_chat_history():
    return st.session_state.get("chat_history", [])

