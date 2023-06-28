from flask import render_template
from flask.views import MethodView


class AccountsHome(MethodView):
    def get(self):
        return render_template('accounts/homepage.html')
