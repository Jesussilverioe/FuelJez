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
        self.assertEqual(checkout, "./templates/checkout.html")

    def test_history(self):
        self.assertEqual(history, history)

    def test_faq(self):
        self.assertEqual(faq, faq)

    def test_create_connection(self):
        self.assertEqual(create_connection, create_connection)

    def test_genON(self):
        self.assertEqual(genON, genON)

    def test_genUniqueID(self):
        self.assertEqual(genUniqueID, genUniqueID)


if __name__ == '__main__':
    unittest.main()
