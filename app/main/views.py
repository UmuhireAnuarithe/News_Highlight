
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



