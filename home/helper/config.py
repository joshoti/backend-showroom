import os

from dotenv import load_dotenv
from flask import Flask

from accounts.views import *
from blog.views import *
from developer.views import *
from home.views import *

load_dotenv()

def create_flask_app(app):
    app = Flask(__name__)

    configuration = get_config_object()
    app.config.from_object(configuration)

    add_url_rules(app)
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

def add_url_rules(app: Flask):
    app.add_url_rule('/', view_func=HomePage.as_view('default homepage'))
    app.add_url_rule('/', view_func=AccountsHome.as_view('accounts subdomain homepage'), subdomain='accounts')
    app.add_url_rule('/', view_func=DeveloperHome.as_view('developer subdomain homepage'), subdomain='developer')
    app.add_url_rule('/', view_func=BlogHome.as_view('blog subdomain homepage'), subdomain='blog')


class Config:
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SERVER_NAME = 'localhost:5000'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True