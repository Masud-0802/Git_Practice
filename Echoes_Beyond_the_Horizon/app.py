import streamlit as st
from quiz import show_quiz

# Page configuration
st.set_page_config(
    page_title="Echoes Beyond the Horizon",
    page_icon="🌌",
    layout="wide"
)

# Load CSS
with open("style.css", "r") as file:
    st.markdown(
        f"<style>{file.read()}</style>",
        unsafe_allow_html=True
    )

# Website heading
st.title("ECHOES BEYOND THE HORIZON")

st.markdown(
    "### Exploring the legacy of NASA's robotic missions"
)

st.write(
    "Discover the stories of four robotic spacecraft "
    "that expanded humanity's understanding of the Moon and Mars."
)

st.divider()

# Mission overview
st.header("The Missions")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌕 Moon Missions")
    st.markdown("""
    - **Surveyor 3:** Robotic lunar lander.
    - **Lunar Prospector:** Lunar orbital mission.
    """)

with col2:
    st.subheader("🔴 Mars Missions")
    st.markdown("""
    - **Spirit:** Mars Exploration Rover.
    - **Opportunity:** Mars Exploration Rover.
    """)

st.divider()

# Interactive quiz
st.header("Test Your Knowledge")

st.write(
    "How well do you know these historic NASA missions? "
    "Take the quiz and find out."
)

show_quiz()