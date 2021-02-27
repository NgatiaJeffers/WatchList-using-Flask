import unittest
from app.models import Review, User

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_james = User(username = 'James', password = 'potato', email = 'james@gmail.com')
        self.new_review = Review(movie_id = 1234, movie_title = 'Python Must Be Crazy Review', image_path = 'https://image.tmdb.org/t/p/w500/jdjdjdjn', 
        movie_review = 'This was whack', user = self.user_james)

    def tearDown(self):
        Review.Clear_reviews()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id, 1234)
        self.assertEquals(self.new_review.movie_title, 'Python Must Be Crazy Review')
        self.assertEquals(self.new_review.image_path, 'https://image.tmdb.org/t/p/w500/jdjdjdjn')
        self.assertEquals(self.new_review.movie_review, 'This was whack')
        self.assertEquals(self.new_review.user, self.user_james)

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all() > 0))

    def test_get_review_by_id(self):
        self.new_review.save_review()
        got_reviews = Review.get_reviews(1234)
        self.asserTrue(len(got_reviews) == 1)