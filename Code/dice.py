#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class rolling dices."""

import random


class Dice():
    "Dice class."

    hard = 6
    medium = 5
    easy = 4
    
    def __init__(self):
        self.rolls_made = 0

    def roll_hard(self):
        "Roll a dice once and return the value."
        self.rolls_made += 1
        return random.randint(3, self.hard)


    def roll_medium(self):
        "Roll a dice once and return the value."
        self.rolls_made += 1
        return random.randint(2, self.medium)

    def roll_easy(self):
        "Roll a dice once and return the value."
        self.rolls_made += 1
        return random.randint(1, self.easy)


    def get_rolls_made(self):
        "Get number of rolls made."
        return self.rolls_made


if __name__ == '__main__':
    dice = Dice()

    roll = dice.roll_hard()
    print("Rolling the dice, it was a {}".format(roll))

    roll = dice.roll_medium()
    print("Rolling the dice, it was a {}".format(roll))

    roll = dice.roll_easy()
    print("Rolling the dice, it was a {}".format(roll))

    number = dice.get_rolls_made()
    print("You have rolled the dice {} times.".format(number))
