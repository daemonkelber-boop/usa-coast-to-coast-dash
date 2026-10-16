# 🏎️ USA Coast-to-Coast Dash!

An educational driving game for 3rd graders. Drive from **New York City to San Francisco**,
collecting stars and fuel on the highway, and solve fun Math, English, Geography, and Graph
challenges at each famous stop (Niagara Falls, Chicago, Mount Rushmore, Yellowstone,
Grand Canyon).

Built with a self-contained HTML/JS game (`game/index.html`) embedded in a
[Streamlit](https://streamlit.io) app (`app.py`).

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

## Editing the quiz questions

Open `game/index.html` and find the `stops` array in the `<script>` section. Each stop
has a `question`, an `options` list, and a `correct` index. The Yellowstone stop also
shows how to add a bar-graph question (`isGraph: true` + `graphData`).

## Controls

- ⬅️ ➡️ arrow keys (or A/D) to steer — click inside the game first so it has keyboard focus
- ⭐ star coin: +25 pts · ⛽ fuel can: +20% fuel · 🚧 cone: −15 pts, −5% fuel
- Correct quiz answer: +100 pts and a full refuel
