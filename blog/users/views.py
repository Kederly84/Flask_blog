from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from flask_login import login_required

users = Blueprint("users", __name__, url_prefix="/users", static_folder="../static")

USERS = {
    1: {"name": "Александр", "age": 38, "nickname": "Kederly"},
    2: {"name": "Екатерина", "age": 36, "nickname": "Kate"},
}


@users.route("/")
@login_required
def user_list():
    return render_template(
        "users/list.html",
        users=USERS
    )


@users.route("/<int:pk>")
@login_required
def get_user(pk: int):
    if pk in USERS:
        user_raw = USERS[pk]
    else:
        raise NotFound("User id:{}, not found".format(pk))
    return render_template(
        "users/details.html",
        user_name=user_raw["name"]
    )


def get_user_name(pk: int):
    if pk in USERS.keys():
        return USERS[pk]
