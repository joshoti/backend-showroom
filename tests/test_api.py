from flask.testing import FlaskClient

from api.views import ApiHealthCheck


def test_health_check(test_client: FlaskClient):
    """Fixture provides application context """
    
    api_response = ApiHealthCheck.get()
    
    assert api_response.status_code == 200
    assert api_response.get_json() == {'message': 'Everything is working fine'}
