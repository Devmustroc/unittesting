from unittest import TestCase
from post import Post


class PostTest(TestCase): # Create a new class that inherits from TestCase
    def test_create_post(self): # Test that we can create a post with a title and content
        p = Post('Test', 'Test Content', 'Author')  # Create a new post object
        self.assertEqual('Test', p.title)  # Assert that the title of the post object is 'Test'
        self.assertEqual('Test Content', p.content)  # Assert that the content of the post object is 'Test Content'
        self.assertEqual('Author', p.author)  # Assert that the author of the post object is 'Author'

    def test_json(self): # Test that the json method of the post object works as expected
        p = Post('Test', 'Test Content', 'Author')  # Create a new post object
        expected = {'title': 'Test', 'content': 'Test Content', 'author': 'Author'}
        self.assertDictEqual(expected, p.json())

    def test_repr(self):
        p = Post('Test', 'Test Content', 'Author')
        self.assertEqual(str(p), 'Test, Author, Test Content')
        self.assertEqual(p.__repr__(), 'Test, Author, Test Content')
        self.assertEqual(p.__str__(), 'Test, Author, Test Content')
