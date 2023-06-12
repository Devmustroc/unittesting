from unittest import TestCase
from unittest.mock import patch
from blog import Blog
import app


class AppTest(TestCase):
    """Test the app module."""

    def test_print_blog(self):
        blog = Blog("Test", "Test Auhtor")
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test by Test Auhtor (0 posts)")

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
