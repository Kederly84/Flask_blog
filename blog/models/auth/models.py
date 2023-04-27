from flask_login import UserMixin
from blog.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)

    def __int__(self, email: str, password: str):
        self.email = email
        self.password = password
