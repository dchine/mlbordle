from flask import Blueprint, flash, redirect, render_template, request, url_for
from .game_logic import get_player
from . import answer


main = Blueprint('main', __name__)
guess_list = []
guess_count = 0
game_answer = answer




@main.route('/')
def index():
    return render_template('index.html')

@main.route('/play', methods=['POST', 'GET'])
def play():
    global guess_list
    global guess_count
    if request.method == 'POST':
        guess = request.form['guess_input']
        if get_player(guess):
            guess_list.append(get_player(guess))
        else:
            flash("Player does not exist!")
        guess_count += 1
        return redirect(url_for('main.play'))
    return render_template('play.html', guess_list=guess_list, answer=game_answer)


