"""USA Coast-to-Coast Dash! - Streamlit wrapper for the 3rd-grade driving game.

The game itself is a self-contained HTML/JS app (game/index.html) that runs
inside a Streamlit embedded component, so the canvas driving, quiz overlays,
and game logic work exactly as designed.
"""
from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html as st_html

st.set_page_config(
    page_title="USA Coast-to-Coast Dash!",
    page_icon="🏎️",
    layout="centered",
)

GAME_HTML_PATH = Path(__file__).parent / "game" / "index.html"

st.title("🏎️ USA Coast-to-Coast Dash!")
st.caption(
    "A 3rd-grade learning road trip: drive from New York City to San Francisco, "
    "solving Math, English, Geography, and Graph challenges at every stop."
)

with st.sidebar:
    st.header("🎮 How to play")
    st.markdown(
        "- Click inside the game once, then steer with ⬅️ ➡️ arrow keys (or A/D)\n"
        "- Collect ⭐ star coins (+25 pts) and ⛽ fuel cans\n"
        "- Avoid 🚧 road cones (−15 pts, −5% fuel)\n"
        "- Answer the challenge at each stop to refuel and keep driving!"
    )
    st.header("📚 Learning goals (3rd grade)")
    st.markdown(
        "- **Math:** division, money subtraction\n"
        "- **English:** proper nouns\n"
        "- **Geography:** US landmarks, directions\n"
        "- **Graphs:** reading bar charts"
    )
    st.header("🗺️ Route")
    st.markdown(
        "NYC → Niagara Falls → Chicago → Mt. Rushmore → "
        "Yellowstone → Grand Canyon → San Francisco"
    )

game_html = GAME_HTML_PATH.read_text(encoding="utf-8")
st_html(game_html, height=600, scrolling=False)

st.divider()
st.caption(
    "Tip: if the arrow keys don't steer, click once inside the game area "
    "to give it keyboard focus."
)
