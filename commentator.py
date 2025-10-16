import streamlit as st
from gtts import gTTS
import random
import os

def run():
    st.header("🎙️ AI Sports Commentator (Offline Mode)")

    # User inputs
    player = st.text_input("Enter Player Name", "Virat Kohli")
    action = st.text_input("Enter Action / Event", "hits a six over midwicket!")
    style = st.selectbox("Commentary Style", ["Excited", "Analytical", "Dramatic", "Calm"])
    language = st.selectbox("Language", ["en", "hi", "es"])

    if st.button("Generate Commentary"):
        if not player.strip() or not action.strip():
            st.warning("⚠️ Please enter both player and action/event.")
            return

        # Offline commentary templates
        templates = {
            "Excited": [
                f"Wow! {player} just {action}! Incredible!",
                f"Unbelievable! {player} {action}! The crowd goes wild!",
                f"Fantastic! {player} {action}! What a moment!"
            ],
            "Analytical": [
                f"{player} {action}. This shows great technique and strategy.",
                f"Analyzing the play, {player}'s {action} was very effective.",
                f"{player} {action}, demonstrating precise skills."
            ],
            "Dramatic": [
                f"In a breathtaking turn, {player} {action}!",
                f"The tension rises as {player} {action}!",
                f"{player} {action}! History might remember this moment!"
            ],
            "Calm": [
                f"{player} {action}. Steady and composed.",
                f"Smooth play by {player}, {action}.",
                f"{player} {action}, nothing rushed, very controlled."
            ]
        }

        # Pick a random commentary from chosen style
        commentary = random.choice(templates.get(style, templates["Excited"]))

        st.subheader("🗣️ Commentary")
        st.write(commentary)

        # Convert to audio
        tts = gTTS(text=commentary, lang=language)
        tts.save("commentary.mp3")
        st.audio("commentary.mp3")
