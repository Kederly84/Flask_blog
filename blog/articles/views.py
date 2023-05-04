from flask import Blueprint, request, render_template, redirect, url_for, current_app
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
from blog.database import db
from blog.users.views import get_user_name
from blog.models import Article, Author
from flask_login import login_required, current_user
from blog.forms.article import CreateArticleForm


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


#
#
# @articles.route("/")
# def articles_list():
#     for article in ARTICLES.keys():
#         raw_author = get_user_name(ARTICLES[article]["author"])
#         if raw_author:
#             ARTICLES[article]["author_name"] = raw_author["name"]
#     return render_template(
#         "articles/list.html",
#         articles=ARTICLES
#     )
#
#
# @articles.route("/<int:pk>")
# def get_article(pk: int):
#     if pk in ARTICLES:
#         article = ARTICLES[pk]
#     else:
#         raise NotFound(f'Article id {pk} not found')
#     title = article["title"]
#     text = article["text"]
#     author = get_user_name(article["author"])
#     return render_template(
#         "articles/detail.html",
#         title=title,
#         text=text,
#         author=author
#     )

@articles.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articles/detail.html", article=article)


@articles.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)
        db.session.add(article)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles.detail", article_id=article.id))
    return render_template("articles/create.html", form=form, error=error)
