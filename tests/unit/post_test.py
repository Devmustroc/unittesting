from unittest import TestCase
from post import Post


class PostTest(TestCase): # Create a new class that inherits from TestCase
    def test_create_post(self): # Test that we can create a post with a title and content
        p = Post('Test', 'Test Content')  # Create a new post object
        self.assertEqual('Test', p.title) # Assert that the title of the post object is 'Test'
        self.assertEqual('Test Content', p.content) # Assert that the content of the post object is 'Test Content'
