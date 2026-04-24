from flask import Flask
from config import Config
from app.database.db import db
import os


def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    app.config.from_object(Config)

    db.init_app(app)


    from app.models.contact import Contact

    from app.routes.contact_routes import contato_bp
    from app.routes.main_routes import main_bp

    app.register_blueprint(contato_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app