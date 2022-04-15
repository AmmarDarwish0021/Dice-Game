#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class rolling dices."""

from pdb import Restart
from player import Player
from AI import AI

class Game:
    """A game class"""

    def __init__(self):
        self.game = []


    def change_name(self, name):
        """Option to change name of a player"""
        print("\nDo you want to change player name?")
        print("Enter \"y\" for yes.")
        print("Enter \"n\" for no.")
        while True:
            choice = input("Make choice: ").lower()
            if choice == "y":
                new_name = input("\nOk. Enter new name: ")
                name = new_name
                break
            elif choice == "n":
                break
            else:
                print("Not a valid choice. Please enter either \"y\" or \"n\".\n")
                continue
        return name


    def next_step(self):
        """Option for next step to take"""
        print("\nEnter \"p\" to start the game.")
        print("Enter \"s\" to show the scores.")
        print("Enter \"c\" to change the name.")
        print("Enter \"r\" to restart the game.")
        print("Enter \"q\" to quit.\n")
        choice = input("Make choice: ").lower()
        return choice
