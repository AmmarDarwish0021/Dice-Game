#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import AI


class TestAIClass(unittest.TestCase):
    "Test the class."""

    def test_init_default_object(self):
        "Instantiate an object and check its properties."""
        ai = AI.AI()
        self.assertEqual(ai.game, 0)

    def test_comp_scores(self):
        """Check if the list length will be 5."""
        ai = AI.AI()
        res0 = ai.comp_scores()

        for x in res0:
            exp0 = 1 <= x <= 6
            self.assertTrue(exp0) 

        exp1 = 5
        res1 = len(res0)
        self.assertEqual(res1, exp1)


if __name__ == '__main__':
    unittest.main()
