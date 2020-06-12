import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.attempts = 2
        self.pin = 777
        self.rise_money = atm_balance

    def test_pin(self):
        self.assertTrue(self.set.enter_pin(777), self.pin)

    


