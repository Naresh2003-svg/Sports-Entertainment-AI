import streamlit as st
import random

def run():
    st.header("🎬 AI Movie/Match Script Generator")

    # Inputs
    match_type = st.selectbox("Select Event Type", ["Cricket Match", "Football Match", "Basketball Match"])
    team1 = st.text_input("Enter Team 1 Name", "Team A")
    team2 = st.text_input("Enter Team 2 Name", "Team B")

    # Generate button
    if st.button("Generate Script"):
        if not team1.strip() or not team2.strip():
            st.warning("Please enter both team names.")
            return

        script = generate_script(match_type, team1, team2)
        st.subheader("📜 Generated Script")
        st.markdown(script)  # Use markdown for line breaks

def generate_script(match_type, team1, team2):
    """Offline script generator using richer templates."""
    
    # Templates with multiple paragraphs for more drama
    templates = {
        "Cricket Match": [
            f"🏏 Today, {team1} faces {team2} in an intense cricket showdown. The stadium is buzzing with anticipation.\n\n"
            f"As the first ball is bowled, tension rises. {team1}'s opening batsman faces {team2}'s fastest bowler. "
            f"Every run counts in this nail-biting match.\n\n"
            f"Midway through the innings, a spectacular catch by {team2} sends the crowd into a frenzy! "
            f"Will {team1} recover and chase the target, or will {team2} defend brilliantly till the last ball?"
        ],
        "Football Match": [
            f"⚽ The stadium is packed as {team1} takes on {team2}. Fans wave flags and cheer loudly, creating a sea of colors.\n\n"
            f"Quick passes, incredible dribbles, and unexpected tackles make this football game a thrill to watch. "
            f"The goalkeepers are on high alert, ready to save the impossible shots.\n\n"
            f"As the match approaches the final minutes, a counterattack by {team1} could change the score dramatically. "
            f"Every kick now could be the winning moment!"
        ],
        "Basketball Match": [
            f"🏀 {team1} vs {team2} promises an electrifying basketball battle. The crowd chants team slogans, building excitement.\n\n"
            f"Every dunk, pass, and 3-pointer keeps everyone on edge. {team1}'s star player faces {team2}'s defensive wall.\n\n"
            f"As the clock ticks down, the score is neck-and-neck. A last-second shot by {team2} could determine the ultimate winner!"
        ]
    }

    # Add an extra random commentary line for more excitement
    extra_comments = [
        "The commentators are going wild with the incredible action unfolding!",
        "Fans are on their feet, shouting and cheering for every play!",
        "The intensity on the field is unmatched; every moment counts!",
        "Drama, tension, and excitement — this is what sports are all about!",
        "History could be made today, as one team strives for glory!"
    ]
    
    base_script = random.choice(templates.get(match_type, ["No script available."]))
    base_script += "\n\n" + random.choice(extra_comments)

    return base_script
