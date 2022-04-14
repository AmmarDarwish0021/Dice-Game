#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Unit testing."

import unittest
import player


class TestPlayerClass(unittest.TestCase):
    "Test the class."

    def test_init_default_object(self):
        "Instantiate an object and check its properties."
        player1 = player.Player()
        self.assertIsInstance(player1, player.Player)

        res1 = player1.name
        exp1 = ''
        self.assertEqual(res1, exp1)

        res2 = player1.dic
        exp2 = {}
        self.assertEqual(res2, exp2)

    def test_scores(self):
        "Roll a dice 5 times and check each value in the list is in bounds"
        player1 = player.Player()
        res0 = 6

        res = player1.scores()
        for x in res:
            exp = 1 <= res0 <= 6
            self.assertTrue(exp)

    def test_highScore(self):
        "Pass list of scores lists and check value is in bounds."
        player1 = player.Player()

        res = player1.highScore()
        exp = 5 <= res <= 30
        self.assertTrue(exp)
    
    # def test_register_results(self, scores1):
    #     "Roll a dice in the medium level and check value is in bounds."
    #     player1 = player.Player()

    #     res = player1.register_results()
    #     for key in res:
    #         for i in value:
    #             exp2 = 2 <= res <= die.medium
    #             self.assertTrue(exp2)

if __name__ == '__main__':
    unittest.main()
