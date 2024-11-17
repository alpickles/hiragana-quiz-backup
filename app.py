from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Hiragana dictionary
hiragana_dict = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}

@app.route('/')
def index():
    return render_template('index.html', hiragana=hiragana_dict)

@app.route('/next_character', methods=['POST'])
def next_character():
    selected_characters = request.json.get('selected_characters', list(hiragana_dict.keys()))
    if not selected_characters:
        return jsonify({'error': 'Please select at least one character to practice.'})

    current_character = random.choice(selected_characters)
    return jsonify({'current_character': current_character})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_input = request.json.get('user_input', '').strip().lower()
    current_character = request.json.get('current_character', '')
    correct_answer = hiragana_dict.get(current_character, '').lower()

    if user_input == correct_answer:
        return jsonify({'feedback': 'Correct!', 'color': 'green'})
    else:
        return jsonify({'feedback': f'Incorrect! The correct answer is: {correct_answer}', 'color': 'red'})

if __name__ == '__main__':
    app.run(debug=True)
