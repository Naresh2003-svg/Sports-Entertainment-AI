import streamlit as st
import random
from PIL import Image

def run():
    st.header("🏅 AI Fantasy Lineup Generator (Offline / With Images)")

    # Select sport
    sport = st.selectbox("Choose a sport", ["Cricket", "Football", "Basketball"])

    st.subheader("Add Players Manually")
    st.write("Enter player details and upload their image:")

    # Store players in session state
    if "players" not in st.session_state:
        st.session_state["players"] = []

    # Input fields
    name = st.text_input("Player Name")
    role = st.text_input("Player Role (Batsman, Forward, Guard, etc.)")
    rating = st.number_input("Player Rating (1-100)", min_value=1, max_value=100, value=80)
    image_file = st.file_uploader("Upload Player Image", type=["jpg", "jpeg", "png"], key="player_img")

    if st.button("Add Player"):
        if name.strip() == "" or role.strip() == "" or image_file is None:
            st.warning("Please enter name, role, and upload an image.")
        else:
            st.session_state["players"].append({
                "name": name,
                "role": role,
                "rating": rating,
                "image": Image.open(image_file).convert("RGB")
            })
            st.success(f"Added {name} ({role}) with rating {rating}")

    # Display current player list with delete option
    if st.session_state["players"]:
        st.subheader("Current Players")
        delete_index = None
        for i, p in enumerate(st.session_state["players"]):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{i+1}. {p['name']} ({p['role']}) - Rating: {p['rating']}")
                if "image" in p and p["image"] is not None:
                    st.image(p["image"], width=100)
            with col2:
                if st.button("❌ Delete", key=f"del_{i}"):
                    delete_index = i  # Mark index to delete

        # Delete after loop to avoid modifying list during iteration
        if delete_index is not None:
            st.session_state["players"].pop(delete_index)
            st.success("Player deleted! Interact with the app to see updated list.")

    # Safe lineup size slider
    num_players = len(st.session_state["players"])
    if num_players > 0:
        if num_players == 1:
            lineup_size = 1  # Only one player available
            st.info("Only one player available, lineup size set to 1")
        else:
            lineup_size = st.slider(
                "Select lineup size",
                min_value=1,
                max_value=num_players,
                value=min(5, num_players)
            )
    else:
        st.info("Add at least one player to generate a lineup.")
        lineup_size = 0

    # Generate lineup
    if st.button("Generate Fantasy Lineup") and num_players > 0:
        # Weighted random selection by rating
        selected_players = random.choices(
            st.session_state["players"],
            weights=[p["rating"] for p in st.session_state["players"]],
            k=lineup_size
        )

        st.subheader(f"🏆 {sport} Fantasy Lineup")
        for i, player in enumerate(selected_players, start=1):
            st.write(f"{i}. {player['name']} ({player['role']}) - Rating: {player['rating']}")
            if "image" in player and player["image"] is not None:
                st.image(player["image"], width=150)

        # Fun explanations
        st.subheader("💡 Why these players were picked:")
        for player in selected_players:
            explanations = [
                f"{player['name']} is known for incredible consistency.",
                f"{player['name']} can turn the game around in crucial moments.",
                f"{player['name']}'s stats make them a top pick for any fantasy lineup.",
                f"{player['name']} has excellent synergy with teammates.",
                f"{player['name']} is a crowd favorite and reliable in big matches."
            ]
            st.write(f"- {random.choice(explanations)}")
