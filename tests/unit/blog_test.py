from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    """
    Test methods in the Blog class.
    """
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        """
        Test that the __repr__ method works as expected.
        """
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)')


    def test_repr_multiple_postes(self):
        """
        Test that the __repr__ method works as expected.
        """
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test', 'another']
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (2 posts)')