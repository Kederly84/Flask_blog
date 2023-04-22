from blog.app import create_app
from blog.settings import PORT, HOST, DEBUG

if __name__ == "__main__":
    app = create_app()
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )
