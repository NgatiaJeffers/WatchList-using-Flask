from app.instance.config import MOVIE_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY 

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    # MOVIE_API_KEY = '7a3b260a2b4a7805cc684ef8de37cf00'
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with  General configuration settings
    '''

    DEBUG = True