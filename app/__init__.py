from flask import Flask
from .datos import datos

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/config.cfg')
    app.register_blueprint(datos)
    return app