document.getElementById('guess-button').addEventListener('click', () => {
    const letter = document.getElementById('guess-input').value;
    if (letter) {
        fetch('/guess', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ letter })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('word-display').textContent = data.display_word;
            document.getElementById('feedback').textContent = data.message;
            document.getElementById('hangman-image').src = data.image;
            if (data.result) {
                document.getElementById('result-message').textContent = data.message;
                document.getElementById('guess-input').disabled = true;
                document.getElementById('guess-button').disabled = true;
            }
        });
    }
    document.getElementById('guess-input').value = '';
});
