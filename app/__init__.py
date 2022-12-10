from flask import Flask
from .config import Config
from app.routes.personaje import personajes_ruta
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(personajes_ruta)

    return app