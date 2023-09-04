import os

from dotenv import load_dotenv
from flask import Flask

from accounts.views import AccountsHome
from api.views import ApiHealthCheck
from blog.views import BlogHome
from developer.views import DeveloperHome
from home.views import HomeIcon, HomePage

load_dotenv()


def create_flask_app(name):
    app = Flask(name)

    configuration = get_config_object()
    app.config.from_object(configuration)

    register_endpoints(app)
    return app


def get_config_object() -> object:
    """ Accepted configuration names are: production, testing, development """

    config_name = os.getenv('CONFIG_TYPE', '')
    config_mapping = {
        "production": ProductionConfig,
        "testing": TestingConfig,
        "development": DevelopmentConfig
    }
    return config_mapping.get(config_name.lower(), ProductionConfig)


def register_endpoints(app: Flask):
    app.add_url_rule('/', view_func=HomePage.as_view('web homepage'))
    app.add_url_rule('/health', view_func=ApiHealthCheck.as_view('app health check'))
    app.add_url_rule('/favicon.ico', view_func=HomeIcon.as_view('web icon'))
    app.add_url_rule('/', view_func=ApiHealthCheck.as_view('api subdomain health check'), subdomain='api')
    app.add_url_rule('/', view_func=AccountsHome.as_view('accounts subdomain homepage'), subdomain='accounts')
    app.add_url_rule('/', view_func=DeveloperHome.as_view('developer subdomain homepage'), subdomain='developer')
    app.add_url_rule('/', view_func=BlogHome.as_view('blog subdomain homepage'), subdomain='blog')


class Config:
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    # SERVER_NAME = 'localhost:5000'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True