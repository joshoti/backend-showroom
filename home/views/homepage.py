from flask import render_template, make_response
from flask.views import MethodView

from api.views import ApiHealthCheck


class HomePage(MethodView):
    def get(self):
        api_response = ApiHealthCheck.get()
        api_data = api_response.get_json()
        api_cookies = api_response.headers.getlist('Set-Cookie')
        
        response = make_response(render_template('home/homepage.html'), api_response.status_code)
        response.headers.extend({'Set-Cookie': api_cookies})
        return response
