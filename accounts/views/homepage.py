from flask.views import MethodView

class AccountsHome(MethodView):
    def get(self):
        return 'Welcome to accounts Homepage'
