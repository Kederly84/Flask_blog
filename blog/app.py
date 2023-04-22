from flask import Flask
from blog.settings import VIEWS


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
