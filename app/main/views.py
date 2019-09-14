
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles,search_article
from .forms import ReviewForm
from ..models import Review


@main.route('/')
def index():
    '''
    View news page function that returns the  news details page and its data
    '''

    Hot_news = get_sources('popular')
    Title = 'Home - Welcome to resourceful news Online Website '
    return render_template('index.html', Title = Title,popular = Hot_news)
    
    
@main.route('/search/<new_Name>')
def search(new_Name):
        new_Name_list = new_Name.split(" ")
        new_Name_format = "+".join(new_Name_list)
        searched_news = search_new(new_Name_format)
        title = f'search articles" for {new_Name}'
        return render_template('search.html',news = searched_news)


@main.route('/new/<id>')
def new_review(id):
        news= get_news(id)
        

        title = 'Article'
        return render_template('news.html',title = title, news=news)