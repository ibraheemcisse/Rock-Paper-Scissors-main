from flask import Flask, request, render_template_string
import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = None
    computer_choice = random.choice(choices)
    result = None

    if request.method == 'POST':
        player_choice = request.form['choice']
        result = determine_winner(player_choice, computer_choice)

    return render_template_string('''
        <!doctype html>
        <html>
        <head><title>Rock, Paper, Scissors</title></head>
        <body>
            <h1>Rock, Paper, Scissors</h1>
            <form method="post">
                <label for="choice">Choose:</label>
                <select id="choice" name="choice">
                    <option value="Rock">Rock</option>
                    <option value="Paper">Paper</option>
                    <option value="Scissors">Scissors</option>
                </select>
                <input type="submit" value="Play">
            </form>
            {% if result %}
                <p>Your choice: {{ player_choice }}</p>
                <p>Computer's choice: {{ computer_choice }}</p>
                <p>Result: {{ result }}</p>
            {% endif %}
        </body>
        </html>
    ''', player_choice=player_choice, computer_choice=computer_choice, result=result)

def determine_winner(player, computer):
    if player == computer:
        return 'It\'s a tie!'
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return 'You win!'
    else:
        return 'You lost!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)