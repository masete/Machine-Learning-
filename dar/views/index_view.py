from flask import render_template
from flask.views import MethodView


class IndexController(MethodView):
    def get(self):
        """Render the home page."""
        return render_template('index.html')

    def post(self):
        return self.get()
