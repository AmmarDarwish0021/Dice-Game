#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import ai_computer
import dice


class TestAi_classClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        aie = ai_computer.Ai_class()
        self.assertIsInstance(aie, ai_computer.Ai_class)
        self.assertEqual(aie.game, 0)

    def test_game_mode_1(self):
        """check if the scores between 1 and 4 in easy mode"""
        aie = ai_computer.Ai_class()
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)
        self.assertIsInstance(aie, ai_computer.Ai_class)
        res = aie.game_mode_1()
        for value in res:
            exp1 = 1 <= value <= 4
            self.assertTrue(exp1)
        res4 = die.roll_easy()
        exp4 = 1 <= res4 <= die.easy
        self.assertTrue(exp4)

    def test_game_mode_2(self):
        """check if the scores between 2 and 5 in medium mode"""
        aie = ai_computer.Ai_class()
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)
        self.assertIsInstance(aie, ai_computer.Ai_class)
        res = aie.game_mode_2()
        for value in res:
            exp2 = 2 <= value <= 5
            self.assertTrue(exp2)
        res3 = die.roll_medium()
        exp3 = 2 <= res3 <= die.medium
        self.assertTrue(exp3)

    def test_game_mode_3(self):
        """check if the scores between 3 and 6 in hard mode"""
        aie = ai_computer.Ai_class()
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)
        self.assertIsInstance(aie, ai_computer.Ai_class)
        list_1 = aie.game_mode_3()
        for value in list_1:
            exp3 = 3 <= value <= 6
            self.assertTrue(exp3)
        res2 = die.roll_hard()
        exp2 = 3 <= res2 <= die.hard
        self.assertTrue(exp2)

if __name__ == '__main__':
    unittest.main()
