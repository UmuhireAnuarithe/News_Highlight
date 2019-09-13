import urllib.request,json
from .models import News_Article,News_source,Review



# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url ='https://newsapi.org/v2/sources?category&apiKey=313d115015d7470998e44f7c461d1ada'


    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_articles = None

        if get_sources_response['results']:
            source_articles_list = get_sources_response['results']
            source_articles = process_results(source_results_list)


    return source_articles






def process_sources(source_list):
    '''
    Function  that processes the source articles result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain articals details

    Returns :
        source_articles: A list of source objects
    '''
    source_articles = []
    for Source in source_list:
               
        id = Source.get('id')   
        source = Source.get('source')  
        description = Source.get('description')  
        url = Source.get('url')  
        country = Source.get('country')  
        language =  Source.get('language')  
        category = Source.get('category')  

        if poster:
            source_object = News_source(id,title,source,description,url,country,language,category)
            source_articles.append(source_object)

    return source_articles



def get_articles(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_article_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        article_list =[]

    if article_details_response['news']:
        for new_article in new_details_response['articles']:
          
            Title = new_article.get('title')
            Author=new_article.get('Author')
            Description=new_article.get('Description')
            url=new_article.get('url')
            urlToImage=new_article.get('urlToImage')
            publishedOn =new_article.get('publishedOn')
            content = new_article.get('content')

            article_object = News_Article(Title,Author,Description,url,urlToImage,publishedOn,content)
            article_list.append(new_object)

    return article_list