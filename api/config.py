import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from .utils import db, ma


def register_extensions(app: Flask):
    db.init_app(app)
    JWTManager(app)
    Migrate(app, db)
    trusted_origins = os.getenv("APPROVED_ORIGINS", "").split(",")
    CORS(app, supports_credentials=True, origins=trusted_origins)
    ma.init_app(app)
