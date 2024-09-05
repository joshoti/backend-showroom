import os

from dotenv import load_dotenv
from flask import Flask

from accounts.views import AccountsHome
from api.config import register_extensions
from api.views import ApiHealthCheck
from blog.views import BlogHome
from developer.views import DeveloperHome
from home.views import HomeIcon, HomePage

load_dotenv()


def create_flask_app(name):
    app = Flask(name)

    configuration = get_config_object()
    app.config.from_object(configuration)

    register_extensions(app)
    register_endpoints(app)
    return app


def get_config_object() -> object:
    """Accepted configuration names are: production, testing, development"""

    config_name = os.getenv("CONFIG_TYPE", "")
    config_mapping = {
        "production": ProductionConfig,
        "testing": TestingConfig,
        "development": DevelopmentConfig,
    }
    return config_mapping.get(config_name.lower(), ProductionConfig)


def register_endpoints(app: Flask):
    app.add_url_rule("/", view_func=HomePage.as_view("web homepage"))
    app.add_url_rule("/favicon.ico", view_func=HomeIcon.as_view("web icon"))
    app.add_url_rule(
        "/v1/api", view_func=ApiHealthCheck.as_view("api subdomain health check")
    )
    app.add_url_rule(
        "/accounts", view_func=AccountsHome.as_view("accounts subdomain homepage")
    )
    app.add_url_rule(
        "/developer", view_func=DeveloperHome.as_view("developer subdomain homepage")
    )
    app.add_url_rule("/blog", view_func=BlogHome.as_view("blog subdomain homepage"))


class Config:
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["headers", "cookies"]


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
