import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.attempts = 2
        self.pin = 777

    def test_replenish(self):
        self.assertEqual(self.set.rise_money(rise_money=3000), 13000)

    def test_replenishing_without_change_balance(self):
        self.assertNotEqual(self.set.rise_money(rise_money=2000), 10000)

    def test_correct_pin(self):
        self.assertTrue(self.set.enter_pin(self.pin))

    def test_incorrect_pin(self):
        self.assertNotEqual(self.set.enter_pin(self.pin), 555)
        self.assertRaises(IncorrectPin)

    # def test_attempts(self):
    #     self.assertNotEqual(self.set.enter_pin(self.pin), 444)
    #     self.assertRaises(IncorrectPin, self.attempts - 1)
        # self.assertNotEqual(self.set.enter_pin(777), self.attempts - 1)
        # self.assertRaises(AttemptsOver)

    def test_withdraw_money(self):
        self.set.enter_pin(self.pin)
        self.assertNotEqual(self.set.get_money(10000), self.balance-5000)
        self.balance = 5000

    def test_withdraw_money_all(self):
        self.set.enter_pin(self.pin)
        self.assertEqual(self.set.get_money(10000), self.balance-0)

    def test_withdraw_money_million(self):
        self.set.enter_pin(self.pin)
        self.assertNotEqual(self.set.get_money(10000), self.balance-1000000)

    def test_correct_balance(self):
        self.assertEqual(self.balance, 10000)

    def test_incorrect_balance(self):
        self.assertNotEqual(self.balance, 50000)


    # def test_attempts_condition(self):
    #     self.assertRaises(AttemptsOver, msg="Attempts are over!!!")
    #     self.set.enter_pin(self.pin)
    #
    # def test_incorrect_condition(self):
    #     self.assertRaises(IncorrectPin, msg="Check Incorrect Pin!!!")
    #     self.set.enter_pin(self.pin)
    #
    # def test_enter_pin_condition(self):
    #     self.assertRaises(EnterPin, msg="Enter pin first!!!")
    #     self.set.enter_pin(self.pin)
    #
    # def test_atm_balance_condition(self):
    #     self.assertRaises(AtmBalance, msg="Atm balance is no enough!!!")
    #     self.set.enter_pin(self.pin)























    


