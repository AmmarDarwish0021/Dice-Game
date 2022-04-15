#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Unit testing."

import unittest
import game


class TestMainClass(unittest.TestCase):
    "Test the class."

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        play = game.Game()
        self.assertIsInstance(play, game.Game)

if __name__ == '__main__':
    unittest.main()
