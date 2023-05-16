from flask import Flask

from blog.settings import VIEWS, login_manager, migrate
from dotenv import load_dotenv
from blog.models.auth.models import User
from blog.database import db


def create_app(config_path) -> Flask:
    app = Flask(__name__)
    load_dotenv(config_path / ".env")
    app.config.from_prefixed_env()
    register_components(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


def register_components(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True, render_as_batch=True)
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
