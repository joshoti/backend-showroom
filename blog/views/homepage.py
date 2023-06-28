from flask.views import MethodView

class BlogHome(MethodView):
    def get(self):
        return "Welcome to blog Homepage"
