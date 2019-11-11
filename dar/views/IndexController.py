from flask import render_template


class Welcome:
    def index(self):
        """Render the home page."""
        return render_template('index.html')