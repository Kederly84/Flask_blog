from flask import Blueprint, render_template

main = Blueprint("main", __name__, url_prefix="/", static_folder="../static")


@main.route("/")
def index_page():
    return render_template("main/main.html")
