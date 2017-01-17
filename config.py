import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_TEARDOWN = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATEBASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'date-dev.sqlite')

config = {
    'development':DevelopmentConfig
}