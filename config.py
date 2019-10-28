import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProdConfig(Config):
    BOOTSTRAP_CDN_FORCE_SSL = True
    PREFERRED_URL_SCHEME = 'https'
    DEBUG = False


class CeleryConfig:
    broker_url = result_backend = os.getenv('REDIS_URL')
    # result_expires = 600
    # broker_transport_options = {'visibility_timeout': 1800}
