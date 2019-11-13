# -*- coding: utf-8 -*-
"""
Main app root of the api endpoints
"""

from flask import Flask
from dar.config.config import HostConfig, ServerConfig, EnvironmentConfig, CeleryConfig
# from dar.config.config import HostConfig, ServerConfig, EnvironmentConfig
from dar.routes import Urls


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

if __name__ == '__main__':
    APP.run(host=HostConfig.HOST, port=HostConfig.PORT)
