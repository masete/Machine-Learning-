import os

from dotenv import load_dotenv

load_dotenv()


class HostConfig:
    """
    System HOST configuration settings
    They can be changed at any time.
    """
    HOST = "0.0.0.0"
    PORT = 5000


class ServerConfig:
    """
    System configuration settings
    They can be changed at any time.
    """
    SECRET_KEY = os.getenv('SECRET_KEY')


class EnvironmentConfig(ServerConfig):
    """
    System configuration settings for running environment
    They can be changed at any time.
    It extends the server congig class
    """
    DEBUG = os.getenv('DEBUG', False)
    TESTING = os.getenv('TESTING', False)
    ENV = os.getenv('ENV', 'production')
    BOOTSTRAP_CDN_FORCE_SSL = True
    PREFERRED_URL_SCHEME = 'https'


class CeleryConfig:
    broker_url = result_backend = os.getenv('REDIS_URL')
    # result_expires = 600
    # broker_transport_options = {'visibility_timeout': 1800}
