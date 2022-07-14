from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from .inicio import inicio
from .usuarios import usuarios
from .datos import datos

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/configuration.cfg')

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .usuarios.models import Usuario
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from .usuarios.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app.register_blueprint(inicio)
    app.register_blueprint(datos)
    app.register_blueprint(usuarios)
    return app