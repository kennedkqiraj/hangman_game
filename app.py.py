from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Hangman game state
game_state = {
    "word": "",
    "display_word": [],
    "wrong_guesses": 0,
    "guessed_letters": []
}

# Hangman images (can be placeholders or real paths to images)
HANGMAN_IMAGES = [
    "/static/hangman0.png", "/static/hangman1.png", "/static/hangman2.png",
    "/static/hangman3.png", "/static/hangman4.png", "/static/hangman5.png",
    "/static/hangman6.png"
]

# List of possible words
WORDS = ["PLANET", "OCEANIC", "DOLPHIN", "JOURNEY", "FREEDOM", "ISLAND","WHISPER",
        "GALAXY",
        "HORIZON",
        "SUNRISE",
        "MYSTERY",
        "EMERALD",
        "ADVENTURE",
        "PHANTOM",
        "FORTRESS",
        "TWILIGHT",
        "STARDUST",
        "WANDERER",
        "HARMONY",
        "CRYSTAL",
        "ENCHANT",
        "ANCIENT",
        "VOYAGER",
        "DESTINY",
        "CHIMERA",
        "CASCADE",
        "PHOENIX",
        "CASCADE",
        "FORTUNE",
        "ALBANIA"]

def start_new_game():
    """Initialize a new game state"""
    game_state["word"] = random.choice(WORDS)
    game_state["display_word"] = ["_"] * len(game_state["word"])
    game_state["wrong_guesses"] = 0
    game_state["guessed_letters"] = []

@app.route('/')
def index():
    start_new_game()
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.json.get("letter").upper()
    if letter in game_state["guessed_letters"]:
        return jsonify({"message": "You already guessed that letter!", "display_word": " ".join(game_state["display_word"]), "wrong_guesses": game_state["wrong_guesses"], "image": HANGMAN_IMAGES[game_state["wrong_guesses"]]})

    game_state["guessed_letters"].append(letter)

    if letter in game_state["word"]:
        for i, char in enumerate(game_state["word"]):
            if char == letter:
                game_state["display_word"][i] = letter
        message = "Correct!"
    else:
        game_state["wrong_guesses"] += 1
        message = "Wrong guess!"

    if "_" not in game_state["display_word"]:
        result = "win"
        message = "Congratulations! You won!"
    elif game_state["wrong_guesses"] >= len(HANGMAN_IMAGES) - 1:
        result = "lose"
        message = f"Game over! The word was: {game_state['word']}"
    else:
        result = None

    return jsonify({
        "message": message,
        "display_word": " ".join(game_state["display_word"]),
        "wrong_guesses": game_state["wrong_guesses"],
        "image": HANGMAN_IMAGES[game_state["wrong_guesses"]],
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
