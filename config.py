from __future__ import annotations

import os


class Config:
    DEBUG = False
    ENV = os.getenv("ENV", "testing")
    FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", "5000")
    print(os.getenv("FLASK_RUN_PORT"))


class DevelopmentConfig(Config):
    ENV = "dev"
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    ENV = "testing"
    DEBUG = True
    TESTING = True
