from flask import Flask
from app.database.db import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #desativa rastreamento e melhora a performance

    db.init_app(app)


    from app.models.contact import Contact

    from app.routes.contato_routes import contato_bp
    from app.routes.main_routes import main_bp

    app.register_blueprint(contato_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app