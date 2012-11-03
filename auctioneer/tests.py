# coding: utf-8
__author__ = 'episage'

import unittest

class MyTestCase(unittest.TestCase):
    #czekaj czekaj, to chyba nie wyjdzie
    # T.
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
