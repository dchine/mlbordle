from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from .game_logic import get_player, get_new_answer, player_names
from . import answer, scheduler
from datetime import datetime


main = Blueprint('main', __name__)

game_answer = answer

def get_daily_game():
    global game_answer
    game_answer = get_new_answer()
    print(game_answer)

scheduler.add_job(id = 'Scheduled Task', func=get_daily_game, trigger="interval", seconds=30)
scheduler.start()

def create_game_session():
    #session.permanent = True
    if 'answer' in session:
        if session['answer'] != game_answer:
            session['guess_list'] = []
            session['guess_count'] = 0
            session['answer'] = game_answer
    else:
        session['answer'] = game_answer
        session['guess_list'] = []
        session['guess_count'] = 0



@main.route('/')
def index():
    return redirect(url_for('main.play'))

@main.route('/play', methods=['POST', 'GET'])
def play():    
    create_game_session()
    if request.method == 'POST':
        guess = request.form['guess_input']
        if get_player(guess):
            session['guess_list'].append(get_player(guess))
            session['guess_count'] += 1
            print(session['guess_list'])
        else:
            flash("Player does not exist!")
        return redirect(url_for('main.play'))
    return render_template('play.html', guess_list=session['guess_list'], answer=game_answer, player_names=player_names)


