#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Unit testing."

import unittest
import game
from player import Player


class TestGameClass(unittest.TestCase):
    "Test the class."

    def test_init_default_object(self):
        "Instantiate an object and check its properties."
        play = game.Game()
        self.assertIsInstance(play, game.Game)

        res2 = play.game
        exp2 = []
        self.assertEqual(res2, exp2)

    def test_change_name(self):
        "Enter  a name and check if the method work as expected"
        play = game.Game()
        exp = input("Enter the name that you expected: ")
        print("\nTo the function:")
        res = play.change_name(exp)
        self.assertEqual(res, exp)

    def test_next_step(self):
        "Call the methon and test if the return valuse one from expected values"
        play = game.Game()
        res = play.next_step()
        exp = {"p", "s", "c", "r", "q"}
        self.assertIn(res, exp)

    def test_restart_the_game(self):
        "Test a clear function with the scores board and the number of wins"
        player = Player()
        comp_player = Player()
        total_wins = 0
        res1 = player.get_the_game_resluts().clear()
        res2 = comp_player.get_the_game_resluts().clear()
        res3 = total_wins
        exp1 = None
        exp2 = None
        exp3 = 0
        self.assertEqual(res1, exp1)
        self.assertEqual(res2, exp2)
        self.assertEqual(res3, exp3)

if __name__ == '__main__':
    unittest.main()
