
from pathlib import Path

from werkzeug.security import generate_password_hash
from blog.database import db
from blog.app import create_app


BASE_DIR = config_path = Path(__file__).resolve().parent

app = create_app(BASE_DIR)


@app.cli.command("init-db", help="create all db")
def init_db():
    db.create_all()


@app.cli.command("create-users", help="create users")
def create_users():
    from blog.models.auth.models import User
    user = User(email="django@django.com", password=generate_password_hash("django"), is_staff=True)
    db.session.add(
        user
    )
    db.session.commit()
