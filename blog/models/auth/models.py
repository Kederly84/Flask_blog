from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from blog.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column

    def __int__(self, email, password, is_staff: bool = False):
        self.email = email
        self.password = password
        self.is_staff = is_staff

    # def is_password_valid(self, pwd):
    #     print(pwd)
    #     print(generate_password_hash(pwd))
    #     print(self.password)
    #     if self.password == generate_password_hash(pwd, method="plain"):
    #         print(True)
    #     return self.password == generate_password_hash(pwd)
