from flask import jsonify
from flask.views import MethodView


class ApiHealthCheck(MethodView):
    @classmethod
    def get(cls):
        response = jsonify({'message': 'Everything is working fine'})
        return response
