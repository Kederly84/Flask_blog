from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.users.views import get_user_name

articles = Blueprint("articles", __name__, url_prefix="/articles", static_folder="../static")

ARTICLES = {
    1: {
        "title": "First title",
        "description": "Some description",
        "text": "Some text",
        "author": 1
    },
    2: {
        "title": "Second title",
        "description": "Another description",
        "text": "Another some text",
        "author": 2
    }
}


@articles.route("/")
def articles_list():
    for article in ARTICLES.keys():
        raw_author = get_user_name(ARTICLES[article]["author"])
        if raw_author:
            ARTICLES[article]["author_name"] = raw_author["name"]
    return render_template(
        "articles/list.html",
        articles=ARTICLES
    )


@articles.route("/<int:pk>")
def get_article(pk: int):
    if pk in ARTICLES:
        article = ARTICLES[pk]
    else:
        raise NotFound(f'Article id {pk} not found')
    title = article["title"]
    text = article["text"]
    author = get_user_name(article["author"])
    return render_template(
        "articles/detail.html",
        title=title,
        text=text,
        author=author
    )
