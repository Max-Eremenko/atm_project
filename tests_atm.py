import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.attempts = 2
        self.pin = 777
        self.rise_money = 0
        # self.client = False

    def test_rise_money(self):
        self.assertTrue(self.set.rise_money(rise_money=0))

    def test_pin(self):
        self.assertTrue(self.set.enter_pin(777))

    def test_pin2(self):
        self.assertTrue(AttemptsOver, self.set.enter_pin(pin=777))

    def test_pin3(self):
        self.assertTrue(IncorrectPin, self.set.enter_pin(pin=777))

    # def test_pin4(self):
    #     self.assertTrue(self.set.enter_pin(pin=777), self.client)

    def test_pin_negative(self):
        self.assertIsNot(self.set.enter_pin(pin=777), self.pin, msg="Check Pin")

    def test_pin_negative1(self):
        self.assertRaises(AttemptsOver, msg="Attempts are over!!!")
        self.set.enter_pin(pin=777)

    def test_pin_negative2(self):
        self.assertRaises(IncorrectPin, msg="Check Incorrect Pin!!!")
        self.set.enter_pin(pin=777)



















    


