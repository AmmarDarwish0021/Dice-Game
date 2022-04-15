#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""An Ai class"""

import dice

class Ai_class:
    """Ai class."""
    def __init__(self):
        """Instantiate an object and its properties."""
        self.game = 0

    def game_mode_1(self):
        """Roll a dice and take five values between 1 and 4"""
        die = dice.Dice()
        list_of_scores = []
        for x_loop in range(5):
            list_of_scores.append(die.roll_easy())
        return list_of_scores

    def game_mode_2(self):
        """Roll a dice and take five values between 2 and 5"""
        die = dice.Dice()
        list_of_scores = []
        for x_loop in range(5):
            list_of_scores.append(die.roll_medium())
        return list_of_scores

    def game_mode_3(self):
        """Roll a dice and take five values between 3 and 6"""
        die = dice.Dice()
        list_of_scores = []
        for x_loop in range(5):
            list_of_scores.append(die.roll_hard())
        return list_of_scores
