from .conftest import create_app


def test_health_check():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')

        assert response.data == b"Welcome to backend-showroom Homepage"
        assert response.status_code == 200


def test_health_check_with_fixtures(test_client):
    response = test_client.get('/')

    assert response.data == b"Welcome to backend-showroom Homepage"
    assert response.status_code == 200