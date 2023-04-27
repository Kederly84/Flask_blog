from pathlib import Path
from blog.app import create_app

BASE_DIR = config_path = Path(__file__).resolve().parent

if __name__ == "__main__":
    app = create_app(BASE_DIR)
    app.run(host="0.0.0.0", port=5000, debug=True)
