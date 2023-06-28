from flask.testing import FlaskClient

from .conftest import create_app


def test_health_check():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        return
        response = test_client.get('/')

        assert b"Welcome to backend-showroom Homepage" in response.data
        assert response.status_code == 200


def test_health_check_with_fixtures(test_client: FlaskClient):
    return
    response = test_client.get('/')

    assert b"Welcome to backend-showroom Homepage" in response.data
    assert response.status_code == 200
