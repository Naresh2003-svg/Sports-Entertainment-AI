import streamlit as st

# Import utils modules
from utils import commentator, memes, fantasy, scripts, music
# Removed: from utils import video_generator

# Streamlit app layout
st.set_page_config(page_title="AI Sports & Entertainment Hub", layout="wide")
st.title("🏆 Generative AI for Sports & Entertainment")

# Sidebar menu
menu = st.sidebar.radio(
    "Select a Feature",
    [
        "AI Sports Commentator 🎙️",
        "AI Sports Meme Generator 😂",
        "AI Fantasy Lineup Generator 🏏⚽",
        "AI Movie/Match Script 🎬",
        "AI Stadium Music 🎶",
        # Removed: "AI Sports Video Generator 🎥",
    ]
)

# Route to utils
if menu == "AI Sports Commentator 🎙️":
    commentator.run()

elif menu == "AI Sports Meme Generator 😂":
    memes.run()

elif menu == "AI Fantasy Lineup Generator 🏏⚽":
    fantasy.run()

elif menu == "AI Movie/Match Script 🎬":
    scripts.run()

elif menu == "AI Stadium Music 🎶":
    music.run()
