from flask import Flask
from flask_apscheduler import APScheduler
from .game_logic import get_new_answer


answer = get_new_answer()
scheduler = APScheduler()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SESSION_COOKIE_NAME'] = "my_session"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    


    return app
