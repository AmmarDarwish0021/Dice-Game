#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""An A_I class"""

import dice

class A_I:
    """A_I class."""

    def __init__(self):
        self.game = 0

    def game_mode_1(self):
        die = dice.Dice()
        list_of_scores = []
        for x in range(5):
            list_of_scores.append(die.roll_easy())
        return list_of_scores

    def game_mode_2(self):
        die = dice.Dice()
        list_of_scores = []
        for x in range(5):
            list_of_scores.append(die.roll_medium())
        return list_of_scores

    def game_mode_3(self):
        die = dice.Dice()
        list_of_scores = []
        for x in range(5):
            list_of_scores.append(die.roll_hard())
        return list_of_scores
