from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string

basedir = Path().resolve()
load_dotenv(basedir / Path(".env"))

CONFIGS = {
    "default": "config.DevelopmentConfig",
    "dev": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
}


def create_app() -> Flask:
    app = Flask(__name__)
    config_name = os.environ.get("ENV", "default")
    try:
        config = import_string(CONFIGS[config_name])()
        app.config.from_object(config)
    except KeyError as e:
        raise KeyError(f"Failed to create app, {config_name!r} isn't a valid environment string", e)

    from flask_bookmark_app.app import bookmark_endpoints

    app.register_blueprint(bookmark_endpoints)

    return app
