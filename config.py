import os
basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigBase(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' \
                              + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

class Development(ConfigBase):
    DEBUG = True
    TESTING = True