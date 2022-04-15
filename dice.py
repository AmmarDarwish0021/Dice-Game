#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class rolling dices."""

import random


class Dice:
    """Dice class."""

    def __init__(self):
        """Instantiate an object and its properties."""
        self.rolls_made = 0
        self.hard = 6
        self.medium = 5
        self.easy = 4

    def roll(self):
        """Roll a die once and return the value."""
        self.rolls_made += 1
        return random.randint(1, self.hard)

    def roll_hard(self):
        """Roll a die once and return the value."""
        self.rolls_made += 1
        return random.randint(3, self.hard)

    def roll_medium(self):
        """Roll a die once and return the value."""
        self.rolls_made += 1
        return random.randint(2, self.medium)

    def roll_easy(self):
        """Roll a die once and return the value."""
        self.rolls_made += 1
        return random.randint(1, self.easy)

    def get_rolls_made(self):
        """Get number of rolls made."""
        return self.rolls_made
