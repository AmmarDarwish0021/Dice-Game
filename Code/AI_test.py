#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""
import unittest
from random import random

import dice
import player
from Code.AI import AI


class TestAIClass(unittest.TestCase):
    "Test the class."""

    def test_init_default_object(self):
        "Instantiate an object and check its properties."""
        ai = AI()
        self.assertEqual(ai.game, 0)

    def test_comp_scores(self):
        """Check if the list length will be 5."""
        ai = AI()
        check1 = ai.comp_scores()
        exp = 5
        res1 = len(check1)
        self.assertEqual(res1, exp)


if __name__ == '__main__':
    unittest.main()
