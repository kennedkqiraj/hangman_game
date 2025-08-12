# Hangman (Flask)

A simple web-based **Hangman** game built with **Flask**.  
The server keeps track of the game state (secret word, guessed letters, wrong guesses) and serves a minimal UI via `index.html`. Clients send guesses to a small JSON API.

## Features
- Random word selection from a curated list
- Progressive hangman images (`/static/hangman{0..6}.png`)
- JSON API for letter guesses
- Simple frontend (Flask template) you can customize

---

## Quick Start

### 1) Clone the repository
```bash
git clone "https://github.com/kennedkqiraj/hangman_game.git"
cd <your-repo>
```

### 2) Create & activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
Create a `requirements.txt` (example below) and install:
```bash
pip install -r requirements.txt
```

**Recommended `requirements.txt`:**
```
Flask>=3.0.0,<4
```

### 4) Project structure (suggested)
```
.
├─ app.py                 # (your Flask code)
├─ requirements.txt
├─ templates/
│  └─ index.html          # UI page
├─ static/
│  ├─ hangman0.png
│  ├─ hangman1.png
│  ├─ hangman2.png
│  ├─ hangman3.png
│  ├─ hangman4.png
│  ├─ hangman5.png
│  └─ hangman6.png
└─ README.md
```

> Make sure you have the images under `static/` with the exact filenames used in the code.

### 5) Run the app

**Option A: run with Python**
```bash
python app.py
```

**Option B: run with Flask CLI**
```bash
# Windows
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

# macOS/Linux
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The app will start on **http://127.0.0.1:5000**.

---

## How it works

The server maintains a single, in-memory game state:

```python
game_state = {
    "word": "",
    "display_word": [],
    "wrong_guesses": 0,
    "guessed_letters": []
}
```

When you open `/`, a new game starts.  
The frontend sends POST requests to `/guess` with a JSON body like `{"letter": "a"}`.

---

## API

### `GET /`
Returns the main HTML page and **starts a new game**.

### `POST /guess`
Submit a single-letter guess.

**Request body**
```json
{ "letter": "a" }
```

**Response**
```json
{
  "message": "Correct!",
  "display_word": "_ A _ _ _",
  "wrong_guesses": 2,
  "image": "/static/hangman2.png",
  "result": null
}
```

- `result` is `"win"` or `"lose"` when the game ends; otherwise `null`.

---

## Notes & Limitations

- **Single-process, global state**: the current implementation stores game state in a global dict. It’s perfect for a local demo but not for multi-user or multi-worker deployments.  
  - For multiple users, store state per session (Flask session), or persist to Redis/DB keyed by session/user.
- **Images**: replace `/static/hangman*.png` with your own assets if you like.
- **Word list**: edit `WORDS` in `app.py` to add/remove words.


## Troubleshooting

- **`ModuleNotFoundError: No module named 'flask'`**  
  You’re likely outside the virtual environment or didn’t install dependencies. Activate `.venv` and run `pip install -r requirements.txt`.

- **Static images not loading**  
  Ensure the images exist under `static/` and the filenames match the list in `HANGMAN_IMAGES`.

- **Port already in use**  
  Run on a different port:  
  ```bash
  flask run --port 5001
  # or
  python app.py  # modify to app.run(port=5001)
  ```

---

## Roadmap / Ideas

- Per-session game state (multiple simultaneous players)
- Scoreboard & history
- Difficulty levels / categories
- Hints & limited retries per hint
- Mobile-friendly UI with CSS framework (Tailwind/Bootstrap)
- Dockerfile & one-command run

---

## License
MIT — feel free to use, modify, and share.

---


