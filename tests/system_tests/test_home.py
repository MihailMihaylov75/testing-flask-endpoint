"""
HomeTests
Home page test cases
"""
__author__ = 'Mihail Mihaylov'

import json

from tests.system_tests.test_base import BaseTests


class TestHomePage(BaseTests):
    """Class testing home page."""
    def test_home_status(self):
        """Test home page status."""
        with self.app() as home:
            response = home.get('/')
            self.assertEqual(response.status_code, 200)

    def test_home_page_json_response(self):
        """Test home page json text."""
        with self.app() as home:
            response = home.get('/')
            self.assertEqual(json.loads(response.get_data()), {'message': 'Hello, world!'})
