"""
Exercise 11
"""

# Import data from another file
from ex10 import *

import unittest

# Create a unit test. In this case we test Mazda class
class OurTest(unittest.TestCase):
    def setUp(self):
        self.the_mazda = Mazda()
    def test1(self):
        self.assertEqual(self.the_mazda.brand(), "mazda")
    def test2(self):
        self.assertEqual(str(self.the_mazda), "this is mazdaaa")
    def test3(self):
        pass
    def tearDown(self):
        pass

# Test Car class
class OurCarTest(unittest.TestCase):
    def setUp(self):
        self.the_car = Car()
    def test1(self):
        self.assertEqual(self.the_car.start(), "started")
    def test2(self):
        self.assertEqual(self.the_car.stop(), "stopped")
    def tearDown(self):
        pass

unittest.main()
