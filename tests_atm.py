import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000

    def test_replenish_balance(self):
        self.assertEqual(self.set.rise_money(rise_money=1), 10001)
        self.assertEqual(self.set.rise_money(rise_money=5000), 15000)
        self.assertEqual(self.set.rise_money(rise_money=10000), 20000)
        self.assertEqual(self.set.rise_money(rise_money=0), 10000)

    def test_withdraw_money(self):
        self.assertNotEqual(self.set.get_money(money=1), 9999)
        self.assertNotEqual(self.set.get_money(money=5000), 5000)
        self.assertNotEqual(self.set.get_money(money=10000), 0)

    def test_withdrawals_above_balance(self):
        self.assertNotEqual(self.set.get_money(money=100000), 0)
        self.assertNotEqual(self.set.get_money(money=50000), 0)
        self.assertNotEqual(self.set.get_money(money=0), 0)
        self.assertRaises(AtmBalance)

    def test_incorrect_balance(self):
        self.assertNotEqual(self.set.check_balance(), 100000000)

    # def test_correct_balance(self):
    #     self.assertFalse(self.set.check_balance(), self.balance)


























    


