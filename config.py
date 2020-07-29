import os
class Config(object):
    SECRET_KEY = 'prueba'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/Academico'
    SQLALCHEMY_TRACK_MODIFICATIONS = False