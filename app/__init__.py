from flask import Flask
from flask_apscheduler import APScheduler
from .game_logic import get_new_answer

answer = get_new_answer()
def get_daily_answer():
    global answers
    answer = get_new_answer()
    print(answer)
    return 

def create_app():

    app = Flask(__name__)
    scheduler = APScheduler()
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    #scheduler.add_job(id = 'Scheduled Task', func=get_daily_answer, trigger="interval", minutes=1)
    #scheduler.start()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
