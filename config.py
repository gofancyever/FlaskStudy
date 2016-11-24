
import os
basedir= os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    BLOG_MAIL_SUBJECT_PREFIX = '[Blog]'
    BLOG_MAIL_SENDER = 'Blog admin <gaooof@hotmail.com>'
    BLOG_ADMIN = os.environ.get('BLOG_ADMIN')
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfit(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.live.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
    'development':DevelopmentConfit,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfit
}

