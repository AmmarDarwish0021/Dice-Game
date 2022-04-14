#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""An AI class"""

import dice
import player


class AI():
    "AI class."

    def __init__(self):
        self.game = 0

    def comp_scores(self):
        die = dice.Dice()
        list_of_scores = []
        while True:
            print("Enter \"1\" for Easy mode.")
            print("Enter \"2\" for Medium mode.")
            print("Enter \"3\" for Hard mode.")
            game_mode = input("Make choice: ").lower()
            if game_mode == "1":
                print("Easy mode selected.")
                for x in range(5):
                    list_of_scores.append(die.roll_easy())
                break
            elif game_mode == "2":
                print("Medium mode selected.")
                for x in range(5):
                    list_of_scores.append(die.roll_medium())
                break
            elif game_mode == "3":
                print("Hard mode selected.")
                for x in range(5):
                    list_of_scores.append(die.roll_hard())
                break
            else:
                print("Not a valid choice. Please enter either \"1\" or \"2\" or \"3\"")
                continue
        return list_of_scores
