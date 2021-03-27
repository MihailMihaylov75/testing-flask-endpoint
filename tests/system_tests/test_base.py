"""
BaseTest
This class should be the parent class to each system test.
It gives each test a Flask test client that we can use.
"""

import unittest
from app import app


class BaseTests(unittest.TestCase):
    """Set up test client for all tests."""

    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client
