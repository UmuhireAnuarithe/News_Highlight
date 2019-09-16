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



# # Getting api key
# api_key = None
# # Getting the news base url
# news_url = None
# sources_url  = None



# def configure_request(app):
#     global api_key,base_news_url,base_source_url
#     api_key=app.config['NEWS_API_KEY']
#     news_url  = app.config['NEWS_API_BASE_URL']
#     sources_url = app.config['NEWS_SOURCES_BASE_URL']

# def get_sources(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_sources_url ='https://newsapi.org/v2/sources?category&apiKey=313d115015d7470998e44f7c461d1ada'


#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         source_articles = None

#         if get_sources_response['results']:
#             source_articles_list = get_sources_response['results']
#             source_articles = process_results(source_results_list)


#     return source_articles






# def process_sources(source_list):
#     '''
#     Function  that processes the source articles result and transform them to a list of Objects
#     Args:
#         source_list: A list of dictionaries that contain articals details
#     Returns :
#         source_articles: A list of source objects
#     '''
#     source_articles = []
#     for Source in source_list:
               
#         id = Source.get('id')   
#         source = Source.get('source')  
#         description = Source.get('description')  
#         url = Source.get('url')  
#         country = Source.get('country')  
#         language =  Source.get('language')  
#         category = Source.get('category')  

#         if poster:
#             source_object = News_source(id,title,source,description,url,country,language,category)
#             source_articles.append(source_object)

#     return source_articles



# def get_articles(id):
#     get_article_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_movie_article_url) as url:
#         article_details_data = url.read()
#         article_details_response = json.loads(article_details_data)

#         article_object = None
#         article_list =[]

#     if article_details_response['news']:
#         for new_article in new_details_response['news']:
          
#             Title = new_article.get('Title')
#             Author=new_article.get('Author')
#             Description=new_article.get('Description')
#             url=new_article.get('url')
#             urlToImage=new_article.get('urlToImage')
#             publishedAt =new_article.get('publishedAt')
#             content = new_article.get('content')

#             article_object = News_Article(Title,Author,Description,url,urlToImage,publishedAt,content)
#             article_list.append(new_object)

#     return article_list

     
# def search_article(new_name):
#     search_new_url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=870c6f91cc3244ac9013dcbecb84e54d?api_key={}&query={}'.format(api_key,new_id)
#     with urllib.request.urlopen(search_new_url) as url:
#         search_new_data = url.read()
#         search_new_response = json.loads(search_new_data)
#         search_new_articles = None

#     if search_new_response['news']:
#         search_new_list = search_new_response['news']
#         search_new_articles = process_articles(search_new_list)
    
#     return search_new_articles

