from unittest import TestCase
from post import Post


class PostTest(TestCase): # Create a new class that inherits from TestCase
    def test_create_post(self): # Test that we can create a post with a title and content
        p = Post('Test', 'Test Content')  # Create a new post object
        self.assertEqual('Test', p.title) # Assert that the title of the post object is 'Test'
        self.assertEqual('Test Content', p.content) # Assert that the content of the post object is 'Test Content'

    # def test_json(self): # Test that the json method of the post object works as expected
    #     p = Post('Test', 'Test Content') # Create a new post object
    #     expected = {'title': 'Test', 'content': 'Test Content'} # Define what the expected result of calling .json() on the post object should be
    #     self.assertDictEqual(expected, p.json()) # Assert that the result of calling .json() on the post object is equal to the expected result
