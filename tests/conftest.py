import os

import pytest

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

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app
