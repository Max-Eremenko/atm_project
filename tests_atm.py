import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.set.client_can_get_money = True

    def test_replenish_balance_on_1(self):
        self.assertEqual(self.set.rise_money(rise_money=1), 10001)

    def test_replenish_balance_on_5000(self):
        self.assertEqual(self.set.rise_money(rise_money=5000), 15000)

    def test_replenish_balance_on_10000(self):
        self.assertEqual(self.set.rise_money(rise_money=10000), 20000)

    def test_withdraw_zero(self):
        self.assertEqual(self.set.rise_money(rise_money=-0), 10000)

    def test_withdraw_multiply_one(self):
        self.assertEqual(self.set.rise_money(rise_money=-1), 9999)

    # def test_withdraw_money(self):
    #     # self.assertEqual(self.set.get_money(money=-1), 9999)
    #     # self.assertEqual(self.set.get_money(money=-5000), 5000)
    #     # self.assertEqual(self.set.get_money(money=-10000), 0)

    # def test_withdrawals_above_balance(self):
    #     self.assertNotEqual(self.set.get_money(money=100000), 0)
    #     self.assertNotEqual(self.set.get_money(money=50000), 0)
    #     self.assertNotEqual(self.set.get_money(money=0), 0)
    #     self.assertRaises(AtmBalance)

    def test_incorrect_balance(self):
        self.assertNotEqual(self.balance, 100000000)

    # def test_correct_balance(self):
    #     self.assertTrue(self.set.check_balance(), self.set.client_can_get_money)

    # def test_6(self):
    #     aa = self.balance - 2000
    #     bb = self.balance - 2000
    #     self.assertEqual(self.balance - 6000)


























    


