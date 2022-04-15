#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class Player"""

import dice

class Player:
    """Player Class"""
    name = ''
    dic = {}

    def __init__(self):
        """Instantiate an object and its properties."""
        self.the_scores = []
        self.name = ''
        self.dic = {}

    def scores(self):
        """Take all scores and put them into a list."""
        die = dice.Dice()
        self.the_scores = []
        for x_loop in range(0, 5):
            value = die.roll(self)
            self.the_scores.append(value)
        return self.the_scores

    def high_score(self, list_of_scores_lists):
        """Taking a list of scores as a parameter and return the highest score."""
        highest_number = 0
        list_of_scores = []
        for a_list in list_of_scores_lists:
            list_of_scores.append(sum(a_list))
        for x_loop in range(len(list_of_scores)):
            if highest_number < list_of_scores[x_loop]:
                highest_number = list_of_scores[x_loop]
        return highest_number

    def register_results(self, scores1):
        """Registering a list of fivr scoresin a dictionary as a value for player name key."""
        if self.name in self.dic:
            self.dic[self.name].append(scores1)
        else:
            self.dic[self.name] = []
            self.dic[self.name].append(scores1)
        return self.dic[self.name]

    def get_the_game_resluts(self):
        """Get the resulting dictionary."""
        return self.dic
