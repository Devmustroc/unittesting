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
