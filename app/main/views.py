
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,get_articles
from .forms import ReviewForm
from ..models import Review


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_source = get_source()
    
    title = "Welcome to News Highlight"
    return render_template('index.html', title = title, sources = news_source)

@main.route('/articles/<articles_id>')
def articles(articles_id):
    '''
    View articles page function that returns artcicles details and its data
    '''
    articles = get_articles()
    return render_template('articles.html',  articles = articles)





# @main.route('/')
# def index():
#     '''
#     View news page function that returns the  news details page and its data
#     '''

#     popular_news = get_source()
#     Title = 'Home - Welcome to resourceful news Online Website '
#     return render_template('index.html', Title = Title,popular = popular_news)
    
    
# @main.route('/search/<article_Name>')
# def search(article_Name):
#         article_Name_list = article_Name.split(" ")
#         article_Name_format = "+".join(article_Name_list)
#         searched_news = search_new(article_Name_format)
#         title = f'search articles" for {article_Name}'
#         return render_template('search.html',news = searched_news)


# @main.route('/article/<id>')
# def new_review(id):
#         news= get_articles(id)
        

#         title = 'Article'
#         return render_template('news.html',title = title, news=news)