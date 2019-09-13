import unittest


from  app import app
from app.models import News_source

class NTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News_source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News_source(12345,'Modern business','http//worldbbussiness/com','Digital based commerce','pa','gekohwgoeg','hit 100k users on their trading')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_source))

if __name__=='__main__':
    unittest.main()