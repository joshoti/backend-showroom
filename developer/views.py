from flask import render_template
from flask.views import MethodView


class DeveloperHome(MethodView):
    def get(self):
        return render_template('developer/tech-blog (developer).html')
        return render_template('developer/homepage.html')
