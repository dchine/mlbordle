from flask import Flask
from flask_apscheduler import APScheduler
from App.game_logic import get_new_answer

answer = {}
def get_daily_answer():
    global answer
    answer = get_new_answer()
    print(answer)
    return 

def create_app():
    global answer

    app = Flask(__name__)
    scheduler = APScheduler()
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    answer = get_new_answer()
    scheduler.add_job(id = 'Scheduled Task', func=get_daily_answer, trigger="interval", minutes=3)
    scheduler.start()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(threaded=True, port=5000)