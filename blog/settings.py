from blog.users.views import users
from blog.main.views import main
from blog.articles.views import articles
from blog.auth.views import auth
from flask_login import LoginManager
from flask_migrate import Migrate

VIEWS = [
    users,
    main,
    articles,
    auth
]

login_manager = LoginManager()

migrate = Migrate()
