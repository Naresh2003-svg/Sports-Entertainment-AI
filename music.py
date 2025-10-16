import streamlit as st
import random

def run():
    st.subheader("🎶 AI Stadium Atmosphere Generator")

    events = ["Goal ⚽", "Six 🏏", "Wicket 🎯", "Victory 🏆", "Close Call 😲"]

    # Crowd messages
    crowd_messages = {
        "Goal ⚽": "Crowd goes WILDD! ⚽🔥",
        "Six 🏏": "Ball out of the park! 🎉🏏",
        "Wicket 🎯": "Stumps shattered! ⚡",
        "Victory 🏆": "Champions! Fireworks everywhere 🎆",
        "Close Call 😲": "Ooohhh! So close 😱"
    }

    sounds = {
    "Goal ⚽": [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3"
    ],
    "Six 🏏": [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3"
    ],
    "Wicket 🎯": [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-17.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-18.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-19.mp3"
    ],
    "Victory 🏆": [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-20.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-21.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-22.mp3"
    ],
    "Close Call 😲": [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-23.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-24.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-25.mp3"
    ]
}


    # Generate button
    if st.button("Generate Stadium Music"):
        st.success("🔥 Stadium Atmosphere Generated 🔥")
        for event in events:
            st.write(f"**{event}**: {crowd_messages[event]}")
            # Pick a random track for this event
            track = random.choice(sounds[event])
            st.audio(track)
