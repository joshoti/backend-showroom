from flask.views import MethodView

class DeveloperHome(MethodView):
    def get(self):
        return "Welcome to developer Homepage"
