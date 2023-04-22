from blog.users.views import users
from blog.main.views import main
from blog.articles.views import articles

DEBUG = True

VIEWS = [
    users,
    main,
    articles
]

HOST = '0.0.0.0'
PORT = 8080
