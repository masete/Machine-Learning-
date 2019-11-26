from wsgiref.simple_server import WSGIServer

from flask import Flask
from flask_bootstrap import Bootstrap

from config.config import HostConfig, ServerConfig, EnvironmentConfig
from routes import Urls


class Server:
    """ Creates flask object to start the server"""

    @staticmethod
    def create_app(config=None, env=None):
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        app.config.update(env.__dict__ or {})
        Urls.generate(app)
        return app


APP = Server().create_app(config=ServerConfig, env=EnvironmentConfig)

Bootstrap(APP)

if __name__ == '__main__':
    http_server = WSGIServer((HostConfig.HOST, HostConfig.PORT), APP)
    http_server.serve_forever()

# run the application using the command
# FLASK_DEBUG=1 FLASK_APP=dar.run:APP flask run
# the FLASK_DEBUG env enables auto reload and logging of debug messages, use only in development
