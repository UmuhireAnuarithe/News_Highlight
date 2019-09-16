

class Source:
    '''
    News_source class to define  News_source  Objects
    '''

    def __init__(self, id, source, description, url, category, language, country):
        self.id = id
        self.source = source
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Article:
    '''
    Article class to define Article objects
    '''
    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


    
class Review:
    '''
    Review class to define  Reviews  Objects
    '''

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response
