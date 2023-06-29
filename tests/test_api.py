from api.views import ApiHealthCheck


def test_health_check():
    api_response = ApiHealthCheck.get()
    
    assert api_response.status_code == 200
    assert api_response.get_json() == {'message': 'Everything is working fine'}
