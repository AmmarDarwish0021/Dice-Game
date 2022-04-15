#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class rolling dices."""

import game


if __name__ == '__main__':
    """The main class and front display of the game. 
    Here players can make decisions and select the game mode they wish to play."""
    play = game.Game()
    print()
    print("            PIG (Dice Game)               ")
    print("-----------------------------------------")
    print("Welcome to PIG. This is a dice game of chance.")
    print("You can roll the dice 5 times. The highest total number wins")
    print("-----------------------------------------\n")
    print("Enter \"s\" for single-player mode.")
    print("Enter \"m\" for multi-player mode.")
    while True:
        game_type = input("Make choice: ").lower()
        if game_type == "m":
            print("Multi-player mode selected.")
            print()
            play.multi_player_game()
            break
        elif game_type == "s":
            print("Single-player mode selected.")
            print()
            play.single_player_game()
            break
        else:
            print("Not a valid choice. Please enter either \"s\" or \"m\"")
