import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.attempts = 2
        self.pin = 777

    def test_replenish_balance(self):
        self.assertEqual(self.set.rise_money(rise_money=3000), 13000)

    def test_withdraw_money(self):
        self.assertNotEqual(self.set.rise_money(rise_money=1000), 9000)

    def test_correct_pin(self):
        self.assertTrue(self.set.enter_pin(self.pin))

    def test_attempts_over(self):
        self.assertTrue(AttemptsOver, self.set.enter_pin(self.pin))

    def test_incorrect_pin(self):
        self.assertTrue(IncorrectPin, self.set.enter_pin(self.pin))

    def test_attempts_condition(self):
        self.assertRaises(AttemptsOver, msg="Attempts are over!!!")
        self.set.enter_pin(self.pin)

    def test_incorrect_condition(self):
        self.assertRaises(IncorrectPin, msg="Check Incorrect Pin!!!")
        self.set.enter_pin(self.pin)

    def test_enter_pin_condition(self):
        self.assertRaises(EnterPin, msg="Enter pin first!!!")
        self.set.rise_money(self.pin)

    def test_atm_balance_condition(self):
        self.assertRaises(AtmBalance, msg="Atm balance is no enough!!!")
        self.set.rise_money(self.pin)

    def test_check_balance(self):
        self.assertEqual(self.balance, 10000)






















    


