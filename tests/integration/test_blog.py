from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    """
    Test methods in the Blog class.
    """

    def test_create_post_in_blog(self):
        """
        Test that we can add a post to the blog.
        """
        b = Blog('Test', 'Test blog')
        b.create_post('Test Post', 'Test blog')
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].author, 'Test blog')

    def test_json_no_posts(self):
        """
        Test that the json method works as expected when no posts have been added.
        """
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': []}
        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test blog')
        expected = {'title': 'Test',
                    'author': 'Test Author',
                    'posts': [
                        {
                            'title': 'Test Post',
                            'content': 'Test blog',
                            'author': 'Test Author'
                         }
                    ]
                    }
        self.assertDictEqual(expected, b.json())
