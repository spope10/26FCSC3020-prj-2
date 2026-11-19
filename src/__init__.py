

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_caching import Cache

db = SQLAlchemy()
login_manager = LoginManager()
cache = Cache()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "development-only-secret"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ctf.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["CACHE_TYPE"] = "SimpleCache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = 300

    db.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)

    login_manager.login_view = "login"

    # Load database models
    from . import models

    # Register application routes
    from .routes import register_routes
    register_routes(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
