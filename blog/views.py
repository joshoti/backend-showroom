from flask import render_template
from flask.views import MethodView


class BlogHome(MethodView):
    def get(self):
        return render_template('blog/social media (blog).html')
        return render_template('blog/homepage.html')
