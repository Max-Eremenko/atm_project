import unittest
from features import *


class TestATM(unittest.TestCase):
    def setUp(self):
        self.set = Atm()
        self.balance = 10000
        self.set.client_can_get_money = True

    def test_replenish_balance_on_1(self):
        self.assertEqual(self.set.rise_money(rise_money=1), 10001)

    def test_replenish_balance_on_4999(self):
        self.assertEqual(self.set.rise_money(rise_money=4999), 14999)

    def test_replenish_balance_on_5001(self):
        self.assertEqual(self.set.rise_money(rise_money=5001), 15001)

    def test_replenish_balance_on_9999(self):
        self.assertEqual(self.set.rise_money(rise_money=9999), 19999)

    def test_replenish_balance_on_10001(self):
        self.assertEqual(self.set.rise_money(rise_money=10001), 20001)

    def test_replenish_balance_on_0(self):
        self.assertEqual(self.set.rise_money(rise_money=0), 10000)

    def test_replenish_balance_on_multiply_1(self):
        self.assertNotEqual(self.set.rise_money(rise_money=-1), 10000)

    # def test_withdrawals_above_balance(self):
    #     self.assertNotEqual(self.set.get_money(money=100000), 0)
    #     self.assertNotEqual(self.set.get_money(money=50000), 0)
    #     self.assertNotEqual(self.set.get_money(money=0), 0)
    #     self.assertRaises(AtmBalance)

    def test_correct_balance(self):
        self.assertTrue(self.set.check_balance(), self.set.client_can_get_money)

    def test_incorrect_balance(self):
        self.assertNotEqual(self.set.check_balance(), 100000000)

    def test_withdraw_0(self):
        aa = self.balance - 0
        # bb = self.balance - 5000
        self.assertEqual(aa, 10000)

    def test_withdraw_1(self):
        aa = self.balance - 1
        self.assertEqual(aa, 9999)

    def test_withdraw_4999(self):
        aa = self.balance - 4999
        self.assertEqual(aa, 5001)

    def test_withdraw_5001(self):
        aa = self.balance - 5001
        self.assertEqual(aa, 4999)

    def test_withdraw_9999(self):
        aa = self.balance - 9999
        self.assertEqual(aa, 1)

    def test_withdraw_10001(self):
        aa = self.balance - 10001
        self.assertEqual(aa, 10000)

    def test_withdraw_multiply_1(self):
        aa = self.balance - -1
        self.assertEqual(aa, 1000)


























    


