import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.attempts = 2
        self.pin = 777
        self.rise_money = 1

    def test_rise_money(self):
        self.assertTrue(self.set.rise_money(rise_money=1), True)

    def test_pin(self):
        self.assertTrue(self.set.enter_pin(777), self.pin)

    def test_pin2(self):
        with self.assertRaises(IncorrectPin, msg="Incorrect Pin!!!"):
            self.set.enter_pin(0)












    


