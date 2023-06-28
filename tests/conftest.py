import os

import pytest
from flask import Flask

from home.helper.config import create_flask_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


def create_app():
    """ Returns a fully configured flask app """

    os.environ['CONFIG_TYPE'] = 'testing'
    app = create_flask_app(__name__)

    # db.init_app(app)
    # jwt.init_app(app)
    # ma.init_app(app)

    # api.add_resource(HealthStatus, '/')
    # api.add_resource(Newsletter, '/newsletter')
    # api.add_resource(Search, '/search')
    # api.add_resource(Projects, "/projects")
    # api.add_resource(ProjectFetch, "/projects/<string:project_id>")
    # api.add_resource(Investment, '/projects/<string:project_id>/invest')
    # api.add_resource(UserRegister, '/register')
    # api.add_resource(UserLogin, '/login')
    # api.add_resource(UserLogout, '/logout')
    # api.add_resource(GoogleAuth, "/auth/google")
    # api.add_resource(GoogleOauthCallback, "/google/oauthcallback")
    # api.add_resource(JWT, '/jwt')
    # api.add_resource(RefreshToken, '/refresh')
    # api.add_resource(ConfirmUser, '/user_confirmation/<string:confirmation_id>')
    # api.add_resource(ConfirmationByUserTest, '/confirmation/user/<string:user_id>')

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app