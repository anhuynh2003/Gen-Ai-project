# app.py


import streamlit as st
from dotenv import load_dotenv
import os
import random
from gtts import gTTS
import base64

from utils.llm_handler import get_llm_response
from utils.spotify_handler import get_track_preview
from utils.reddit_handler import get_reddit_advice
from utils.books_handler import search_books
from utils.quote_handler import get_book_quote
from utils.emotion_detector import detect_emotion
from utils.journaling_prompts import get_prompt_by_emotion
from utils.crisis_detector import is_crisis
from utils.insight_classifier import classify_topic
from utils.conversation_memory import initialize_chat, add_to_chat, get_chat_history

# --- Load env + init chat ---
load_dotenv()
initialize_chat()

# --- Session state setup ---
if "mode" not in st.session_state:
    st.session_state.mode = None
if "confirmed_mode" not in st.session_state:
    st.session_state.confirmed_mode = False

# --- Page config ---
st.set_page_config(page_title="MoodMuse.ai", page_icon="🧠")
st.title("🧠 MoodMuse AI Agent")
st.markdown("## How can I support you today?")

# --- Helper: Text-to-Speech ---
def text_to_speech_base64(text):
    tts = gTTS(text)
    tts.save("quote.mp3")
    with open("quote.mp3", "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode()

# --- Helper: Display quote and audio ---
def display_audio_quote():
    st.subheader("🎧 Spoken Wisdom")
    book_quote = get_book_quote()
    st.markdown(f"**📖 Quote:** *{book_quote}*")
    audio_b64 = text_to_speech_base64(book_quote)
    audio_html = f"""
    <audio controls autoplay>
        <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- Step 1: Mode Selection ---
if not st.session_state.confirmed_mode:
    st.session_state.mode = st.selectbox(
        "Choose an experience:",
        ("I want to be heard", "I want a fun distraction", "🎲 Surprise Me!")
    )

    if st.button("Start", key="start_mode_button"):
        if st.session_state.mode == "🎲 Surprise Me!":
            st.session_state.mode = random.choice(["I want to be heard", "I want a fun distraction"])
            st.success(f"🎉 Surprise! You got: **{st.session_state.mode}**")
        st.session_state.confirmed_mode = True
        st.experimental_rerun()

# --- Step 2: Show Mode Content ---
else:
    mode = st.session_state.mode

    if mode == "I want to be heard":
        user_input = st.text_area("What's on your mind?", height=150)
        if st.button("Reflect"):
            if user_input.strip() == "":
                st.warning("Please enter something for the AI to respond to.")
            else:
                with st.spinner("Thinking..."):
                    emotion = detect_emotion(user_input)
                    topic = classify_topic(user_input)
                    crisis = is_crisis(user_input)
                    response = get_llm_response(user_input)
                    prompt = get_prompt_by_emotion(emotion)
                    add_to_chat(user_input, response)

                st.success("Here's what the AI therapist says:")
                st.write(response)

                if crisis:
                    st.error("⚠️ If you're in crisis, call the SLO County Mobile Crisis Team at 1-800-783-0607.")

                st.info(f"**Emotion Detected:** {emotion}  |  **Topic:** {topic}")
                st.markdown(f"**📝 Journaling Prompt:** {prompt}")
                display_audio_quote()

                st.write("---")
                st.subheader("🧵 Chat History")
                for msg in get_chat_history():
                    st.markdown(f"**You:** {msg['user']}")
                    st.markdown(f"**AI:** {msg['ai']}")

    elif mode == "I want a fun distraction":
        st.subheader("🎵 Song Vibes")
        track_query = st.text_input("Type a song or mood:")
        if st.button("Suggest Song"):
            if track_query.strip():
                with st.spinner("Finding your song..."):
                    st.write(get_track_preview(track_query))
            else:
                st.warning("Please enter something!")

        display_audio_quote()

        st.subheader("🔍 Book Search")
        book_query = st.text_input("Book topic or keyword:")
        if st.button("Search Books"):
            if book_query.strip():
                with st.spinner("Searching books..."):
                    for book in search_books(book_query):
                        st.markdown(book)
            else:
                st.warning("Please enter a keyword.")

        st.subheader("🧵 Reddit Life Advice")
        reddit_keyword = st.text_input("Mood or keyword for advice:")
        if st.button("Search Reddit Advice"):
            if reddit_keyword.strip():
                with st.spinner("Browsing Reddit..."):
                    for advice in get_reddit_advice(reddit_keyword):
                        st.markdown(f"- {advice}")
            else:
                st.warning("Please enter a keyword.")

# --- Back to Home Button in Sidebar ---
with st.sidebar:
    st.markdown("## Navigation")
    if st.session_state.confirmed_mode:
        if st.button("Back to Home", key="back_home"):
            st.session_state.mode = None
            st.session_state.confirmed_mode = False
            st.experimental_rerun()
    st.markdown("---")
    st.caption("Need a fresh start?")



