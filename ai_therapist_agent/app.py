# app.py

import streamlit as st
from dotenv import load_dotenv
import os

from utils.llm_handler import get_llm_response
from utils.spotify_handler import get_track_preview
from utils.reddit_handler import get_reddit_advice
from utils.books_handler import search_books
from utils.emotion_detector import detect_emotion
from utils.quote_handler import get_comforting_quote
from utils.journaling_prompts import get_prompt_by_emotion
from utils.crisis_detector import is_crisis
from utils.insight_classifier import classify_topic
from utils.conversation_memory import initialize_chat, add_to_chat, get_chat_history

# Load environment variables
load_dotenv()

# Initialize chat memory
initialize_chat()

# Page setup
st.set_page_config(page_title="AI Therapist", page_icon="🧠")
st.title("🧠 AI Therapist Agent")
st.write("Tell me what you're feeling, and I'll reflect with care and empathy.")

# User input
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
            quote = get_comforting_quote()
            prompt = get_prompt_by_emotion(emotion)
            add_to_chat(user_input, response)

        st.success("Here's what the AI therapist says:")
        st.write(response)

        if crisis:
            st.error("⚠️ This message might contain signs of emotional distress. If you're in crisis, please reach out to the 1-800-783-0607, SLO County Mobile Crisis Team.")

        st.info(f"**Emotion Detected:** {emotion}  |  **Topic:** {topic}")
        st.markdown(f"**📝 Journaling Prompt:** {prompt}")
        st.markdown(f"**💬 Comforting Quote:** *{quote}*")

        st.write("---")
        st.subheader("🧵 Chat History")
        for msg in get_chat_history():
            st.markdown(f"**You:** {msg['user']}")
            st.markdown(f"**AI:** {msg['ai']}")

# --- Spotify Section ---
st.write("---")
st.subheader("🎵 Song Vibes")
track_query = st.text_input("Type a song or mood to match your vibe:")
if st.button("Suggest Song"):
    if track_query.strip() == "":
        st.warning("Enter something to search for.")
    else:
        with st.spinner("Finding your song..."):
            track_info = get_track_preview(track_query)
            st.write(track_info)

# --- Reddit Advice Section ---
st.write("---")
st.subheader("🧵 Internet Advice")
if st.button("Get Reddit Advice"):
    with st.spinner("Browsing Reddit..."):
        advice = get_reddit_advice()
        st.markdown(f"**Reddit says:** {advice}")

# --- Book Quote Section ---
st.write("---")
st.subheader("📚 Book Wisdom")
if st.button("Suggest a Book Quote"):
    with st.spinner("Flipping pages..."):
        book_quote = get_book_quote()
        st.markdown(f"**📖 Quote:** {book_quote}")
