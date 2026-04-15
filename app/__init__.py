from flask import Flask
from app.database.db import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #desativa rastreamento e melhora a performance

    db.init_app(app)

    return app