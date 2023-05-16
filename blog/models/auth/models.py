from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column
    author = relationship("Author", uselist=False, back_populates="user")

    def __int__(self, email, password, is_staff: bool = False):
        self.email = email
        self.password = password
        self.is_staff = is_staff


class Author(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="author")
    articles = relationship("Article", back_populates="author")
