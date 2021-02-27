import os
# from app.instance.config import MOVIE_API_KEY, SECRET_KEY

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-access:Access@localhost/watchlist'
    UPLOADED_PHOTOS_DEST = 'app/static/photos' 
    # email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with  General configuration settings
    '''


class TestConfig(Config):
    '''
    Connecting to our test database
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-access:Access@localhost/watchlist_test'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-access:Access@localhost/watchlist'


    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}