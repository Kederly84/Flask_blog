from blog.users.views import users
from blog.main.views import main
from blog.articles.views import articles
from blog.auth.views import auth
from flask_login import LoginManager
from flask_migrate import Migrate
from blog.authors.views import authors_app

VIEWS = [
    users,
    main,
    articles,
    auth,
    authors_app
]

login_manager = LoginManager()

migrate = Migrate()
