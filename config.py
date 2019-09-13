import os

class Config:
    '''
    genreral configuration for  parent  class
    '''

NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'   
NEWS_API_KEY = os.environ.get('313d115015d7470998e44f7c461d1ada')
SECRET_KEY = os.environ.get('SECRET_KEY')
NEWS_SOURCES_BASE_URL='https://newapi.org/v2/sources?category&apiKey=313d115015d7470998e44f7c461d1ada'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


# 313d115015d7470998e44f7c461d1ada