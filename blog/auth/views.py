from flask import Blueprint, request, render_template, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from blog.database import db
from blog.forms.user import RegistrationForm, LoginForm
from blog.models.auth.models import User

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder="../static")


# @auth.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "GET":
#         return render_template("auth/login.html")
#     email = request.form.get("email")
#     password = request.form.get("password")
#     user = User.query.filter_by(email=email).first()
#
#     if not user or not check_password_hash(user.password, password):
#         flash("Check your login or password")
#         return redirect(url_for(".login"))
#     login_user(user)
#     return redirect(url_for("main.index_page"))


@auth.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.main"))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        print(f'Email {form.email.data}')
        print(f'PWD {form.password.data}')
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form, error="Email not found")
        if not check_password_hash(user.password, form.password.data):
            return render_template("auth/login.html", form=form, error="Invalid email or password")
        login_user(user)
        return redirect(url_for("main.main"))
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))


@auth.route("/register", methods=["POST", "GET"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect("index")
    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)
        user = User(
            email=form.email.data,
            is_staff=False,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("main.main"))
    return render_template("auth/register.html", form=form, error=error)
