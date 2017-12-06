from django.test import TestCase
from .models import User, Image, tags

class UserTestClass(TestCase):
    # set up method
    def setUp(self):
        self.gitu = User(first_name = 'Gitu', last_name = 'Mbugua', email = 'gitu@testing.com', phone_number = '0700123456')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gitu, User))

    # save method
    def test_save_method(self):
        self.gitu.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        # create new user instance and save
        self.gitu = User(first_name = 'Gitu', last_name = 'Mbugua', email = 'gitu@testing.com', phone_number = '0700123456')
        self.gitu.save_user()

        # create new tag and save
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        # create new image instance and save
        self.new_image = Image(photo = 'photo/url.image', author = self.gitu)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        User.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()

    # def test_get_images(self):
    #     images = Image.get_images()
    #     self.assertTrue(len(get_images) > 0)

class tagsTestClass(TestCase):
    '''
    Test case for tags class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a tags instance before each test
        '''
        # Create a tags instance
        self.new_tag = tags(name='Python')

    def test_search_by_tags(self):
        '''
        Test case to check if tags containg a search term is gotten from the database 
        '''
        self.new_tag.save_tags()
        found_tags = tags.search_by_tags('Python')
        self.assertTrue( len(found_tags) == 1)