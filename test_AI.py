#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import A_I
import dice


class TestA_IClass(unittest.TestCase):
    "Test the class."""

    def test_init_default_object(self):
        "Instantiate an object and check its properties."""
        aie = A_I.A_I()
        self.assertIsInstance(aie, A_I.A_I)
        self.assertEqual(aie.game, 0)

    def test_game_mode_1(self):
        aie = A_I.A_I()
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)
        self.assertIsInstance(aie, A_I.A_I)
        res = aie.game_mode_1()
        for x in res:
            exp1 = 1 <= x <= 4
            self.assertTrue(exp1)
        res4 = die.roll_easy()
        exp4 = 1 <= res4 <= die.easy
        self.assertTrue(exp4)

    def test_game_mode_2(self):
        aie = A_I.A_I()
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)
        self.assertIsInstance(aie, A_I.A_I)
        res = aie.game_mode_2()
        for x in res:
            exp2 = 2 <= x <= 5
            self.assertTrue(exp2)
        res3 = die.roll_medium()
        exp3 = 2 <= res3 <= die.medium
        self.assertTrue(exp3)

    def test_game_mode_3(self):
        aie = A_I.A_I()
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)
        self.assertIsInstance(aie, A_I.A_I)
        list_1 = aie.game_mode_3()
        for x in list_1:
            exp3 = 3 <= x <= 6
            self.assertTrue(exp3)
        res2 = die.roll_hard()
        exp2 = 3 <= res2 <= die.hard
        self.assertTrue(exp2)

if __name__ == '__main__':
    unittest.main()
