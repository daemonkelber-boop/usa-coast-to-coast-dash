# 🏎️ USA Coast-to-Coast Dash!

An educational driving game for 3rd graders. **Choose your own road trip** on the
US map — tap any start city and any end city, and the game builds the route,
pit stops, roadside landmarks, and fresh quiz questions for that exact trip.

Drive in a landscape view past real landmarks, collecting stars and fuel on the
highway, and solve **brand-new** Math, English, Geography, and Graph challenges
at every stop (questions are generated fresh every run — see below).

Built with a self-contained HTML/JS game (`game/index.html`) embedded in a
[Streamlit](https://streamlit.io) app (`app.py`). Also playable directly via
GitHub Pages.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy it free (Streamlit Community Cloud)

1. Push this repo to GitHub (or fork it).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app** → pick this repo, branch `main`, and `app.py` as the main file.
4. Deploy — you'll get a public `*.streamlit.app` link to share.

## Project structure

```
usa-coast-to-coast-dash/
├── app.py            # Streamlit wrapper (title, sidebar, embeds the game)
├── game/
│   └── index.html    # The full game: canvas driving + quiz challenges
├── requirements.txt
└── README.md
```

## Choose-your-own-route

The trip starts on a clickable US map (`#route-overlay` in `game/index.html`):
tap a start city 🟢 then an end city 🏁 (or hit 🎲 Surprise Me). `buildRoute()`
finds cities along the start→end corridor, orders them geographically, and
assigns quiz subjects (Math → English → Geography → Graphs) to the stops.
`buildRouteCtx()` then feeds the actual city names, states, landmarks, and the
trip's compass direction into the question generator — so Geography questions
ask about *your* route's capitals and landmarks, and Math/English questions
name *your* stops.

To add a city, add an entry to the `CITIES` array (name, state, x/y on the
0–100 map grid, landmark emoji, scenery). To tweak routing, see the corridor
/ detour logic in `buildRoute()`.

## Infinite question generator

Quiz questions are **generated fresh every run** by the built-in generator in
`game/index.html` (the `QG` object in the `<script>` section) — no API key, no
internet needed, and kid-safe by design. Each stop has a subject (Math,
English, Geography, Graphs) and the generator picks a random template with
randomized numbers, words, and charts.

To add a new question template, add a function to the right subject array in
`QG`. Each function returns `{ q, opts, expl }` where `opts` comes from the
`buildOptions(correctText, distractTexts)` helper (it guarantees 4 distinct
options with one correct answer, shuffled).

## Controls

- 🗺️ tap start/end cities on the map (or 🎲 Surprise Me), then pick your car — race car, sedan, SUV, van, truck, or bus — and its color in the garage
- ⬅️ ➡️ arrow keys (or A/D) to steer — click inside the game first so it has keyboard focus
- 👆 touch: press and hold the LEFT or RIGHT half of the road to steer
- ⭐ star: +25 pts · 🚗 traffic: dodge it! −15 pts, −5% fuel on a hit
- Correct quiz answer: full refuel +100 pts · wrong answer: −20 pts, −10% fuel (fuel comes ONLY from correct answers!)
- Landmarks (🌊 🏙️ 🗿 🌋 🏜️ 🌉) appear on the roadside as you approach each stop
