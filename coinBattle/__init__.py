
from flask import Flask
from flask_socketio import SocketIO

socket = SocketIO()
def create_app():
    app = Flask(__name__, static_folder="static", template_folder="template")

    app.secret_key = "YOTDARK_SECERT_KEY"
    from coinBattle.com.home.controller import HomeController
    app.register_blueprint(HomeController.bp)

    socket.init_app(app)


    return app
