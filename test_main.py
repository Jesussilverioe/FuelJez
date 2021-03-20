import unittest
import pytest
from main import *


class TestingMain(unittest.TestCase):
    def test_index(self):
        self.assertEqual(index, index)

    def test_create_profile(self):
        self.assertEqual(create_profile, create_profile)

    def test_quotes(self):
        self.assertEqual(quotes, quotes)

    def test_checkout(self):
        self.assertEqual(checkout, checkout)

    def test_history(self):
        self.assertEqual(history, history)

    def test_faq(self):
        self.assertEqual(faq, faq)

if __name__ == '__main__':
    unittest.main()
