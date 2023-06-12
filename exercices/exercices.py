import unittest
from unittest.mock import patch

class MyClass:
    def __init__(self):
        self.value = 42

class MyTestCase(unittest.TestCase):
    @patch('__main__.MyClass.value')
    def test_something(self, mock_value):
        # Using patch to replace the value attribute with a mock
        mock_value.return_value = 10

        obj = MyClass()
        result = obj.value
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
