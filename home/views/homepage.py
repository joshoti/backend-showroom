from flask.views import MethodView

class HomePage(MethodView):
    def get(self):
        return "Welcome to backend-showroom Homepage"