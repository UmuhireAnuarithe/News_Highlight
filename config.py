import os

class Config:
    '''
    genreral configuration for  parent  class
    '''

    NEWS_SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?apiKey=313d115015d7470998e44f7c461d1ada' 
    NEWS_ARTICLES_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=313d115015d7470998e44f7c461d1ada'  
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
# SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
