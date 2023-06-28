from flask.views import MethodView

class ApiHealthCheck(MethodView):
    def get(self):
        return {'message': 'Everything is working fine'}
