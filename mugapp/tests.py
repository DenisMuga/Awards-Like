from django.test import TestCase
from .models import*

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='denis', password='denis1234')
        self.user.save()
        
    def test_instance(self):
            self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='denis')
        self.post = Post.objects.create(id=1, title='Delani Studio', photo='https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg', desc='A program in html css and js',
                                        user=self.user, url='https://denismuga.github.io/Delani-Studio/')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)


class RatingTest(TestCase):
    def setUp(self):
        def setUp(self):
            self.user = User.objects.create(id=1, username='denis')
            self.post = Post.objects.create(id=1, title='Github Search', photo='https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg', desc='A program in html css and js',
                                        user=self.user, url='https://denismuga.github.io/Angular-Week2IP/profiles/profiles')
            self.rating = Rating.objects.create(id=1, design=4, usability=8, content=7, user=self.user, post=self.post)
            
        def test_instance(self):
            self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)
