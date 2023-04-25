from flask import Blueprint, request, render_template, flash, redirect, url_for
from blog.models.auth.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder="../static")


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Check your login or password")
        return redirect(url_for(".login"))
    login_user(user)
    return redirect(url_for("main.index_page"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
