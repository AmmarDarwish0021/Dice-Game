#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Unit testing."

import unittest
import dice


class TestDiceClass(unittest.TestCase):
    "Test the class."

    def test_init_default_object(self):
        "Instantiate an object and check its properties."
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res1 = die.hard
        exp1 = 6
        self.assertEqual(res1, exp1)

        res2 = die.medium
        exp2 = 5
        self.assertEqual(res2, exp2)

        res3 = die.easy
        exp3 = 4
        self.assertEqual(res3, exp3)


    def test_roll_a_dice(self):
        "Roll a dice and check value is in bounds."
        die = dice.Dice()

        res0 = die.roll()
        exp0 = 1 <= res0 <= die.hard
        self.assertTrue(exp0)

    def test_roll_a_dice_hard(self):
        "Roll a dice in the hard level and check value is in bounds."
        die = dice.Dice()

        res1 = die.roll_hard()
        exp1 = 3 <= res1 <= die.hard
        self.assertTrue(exp1)
    
    def test_roll_a_dice_medium(self):
        "Roll a dice in the medium level and check value is in bounds."
        die = dice.Dice()

        res2 = die.roll_medium()
        exp2 = 2 <= res2 <= die.medium
        self.assertTrue(exp2)
    
    def test_roll_a_dice_easy(self):
        "Roll a dice in the easy level and check value is in bounds."
        die = dice.Dice()

        res3 = die.roll_easy()
        exp3 = 1 <= res3 <= die.easy
        self.assertTrue(exp3)


if __name__ == '__main__':
    unittest.main()
