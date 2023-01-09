from __future__ import annotations

from flask_bookmark_app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
