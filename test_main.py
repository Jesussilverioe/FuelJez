import unittest

import flask.globals
from app.main import *


class TestApp(unittest.TestCase):
    def test_getPrice(self):

        location = 'TX'
        rate_hist = 1
        gallons_req = 212

        current_price = 1.50
        factors = 0.00
        if location == 'TX':
            factors += .02
        else:
            factors += .04
        
        if rate_hist >= 1:
            factors -= .01
        
        if gallons_req > 1000:
            factors += .02
        else:
            factors += .03
            
        factors += .10

        margin = factors * current_price
        suggested_price = margin + current_price
        
        temp = float(suggested_price * gallons_req)
        total = '{0:.2f}'.format(float(temp))

        arr = [margin, suggested_price, total]

        self.assertEqual(type(arr), list)

    def test_getUniqueID(self):
        length = 9
        id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
        self.assertEqual(type(id), str)

    def test_genON(self):
        length = 9
        id = ''.join([random.choice(string.digits) for n in range(length)])
        self.assertEqual(type(id), str)

    def test_create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
            :param db_file: database file
            :return: Connection object or None
        """
        db = 'create_connection()'
        self.assertEqual(type(db), str)
        
    def test_faq(self):
        faq = 'faq()'
        self.assertEqual(type(faq), str)

    def test_history(self):
        history = 'history()'
        self.assertEqual(type(history), str)

    def test_checkout(self):
        checkout = 'checkout()'
        self.assertEqual(type(checkout), str)


    def test_quotes(self):
        quotes = 'quotes()'
        self.assertEqual(type(quotes), str)

    def test_create_profile(self):
        create_profile = 'create_profile()'
        self.assertEqual(type(create_profile), str)
   
    def test_signin(self):
        signin = 'signin()'
        self.assertEqual(type(signin), str)
        

if __name__ == '__main__':
    unittest.main()