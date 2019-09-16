import urllib.request,json
from .models import Article,Source,Review


#Getting api key
api_key = None

#Getting the news base url
base_source_url = None
base_article_url = None

def configure_request(app):
    global api_key, base_article_url, base_source_url
    api_key = app.config['NEWS_API_KEY']
    base_source_url = app.config['NEWS_SOURCE_API_BASE_URL']
    base_article_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_source_url.format(api_key)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        print(get_source_response)
        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_source(source_results_list)

    return source_results


def process_source(source_list):
    '''
    Function  that processes the source results and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain movie details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id, name, description, url, category, language, country)
        source_results.append(source_object)
        
        # source_results.append(Source(id, name, description, url, category, language, country))

    return source_results




def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_article_url.format('everything', api_key) + "&sources="

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        articles_results.append(Article(id, name, author, title, description, url, urlToImage, publishedAt))

    return articles_results


