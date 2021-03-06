#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class rolling dices."""

from player import Player
import ai_computer


def comp_scores():
    """The user will be able to choose which difficulty they want for the game.
    Depending on the choice, the game will call different functions from the AI class.
    One function for easy role, another for medium role, another for hard role."""
    aie = ai_computer.Ai_class()
    list_of_scores = []
    while True:
        print("\nEnter \"1\" for Easy mode.")
        print("Enter \"2\" for Medium mode.")
        print("Enter \"3\" for Hard mode.\n")
        game_mode = input("Make choice: ").lower()
        if game_mode == "1":
            print("Easy mode selected.\n")
            list_of_scores = aie.game_mode_1()
            break
        elif game_mode == "2":
            print("Medium mode selected.\n")
            list_of_scores = aie.game_mode_2()
            break
        elif game_mode == "3":
            print("Hard mode selected.\n")
            list_of_scores = aie.game_mode_3()
            break
        else:
            print("Not a valid choice. Please enter either \"1\" or \"2\" or \"3\"")
            continue
    return list_of_scores


def next_step():
    """Option for next step to take"""
    print("\nEnter \"p\" to start the game.")
    print("Enter \"s\" to show the scores.")
    print("Enter \"c\" to change the name.")
    print("Enter \"r\" to restart the game.")
    print("Enter \"q\" to quit.\n")
    choice = input("Make choice: ").lower()
    return choice


def change_name(name):
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


def single_player_game():
    """Single player game functionality. Receive name input and set to the player.
        As long as player does not choose restart or quit options, game will continue to be played.
        Player can choose to change name during the game.
        Player can also choose to display scores"""
    player = Player()
    comp_player = Player()
    total_wins = 0
    comp_player.name = "Computer"
    player.name = input("Choose a player name: ")

    while True:
        choice = next_step()
        if choice == "q":
            print("Exit the game..\n")
            break
        elif choice == "r":
            print("Restart The game...\n")
            player.get_the_game_resluts().clear()
            comp_player.get_the_game_resluts().clear()
            continue
        elif choice == "p":
            print("Start the game: \n")
            comp_score = comp_scores()
            list_of_scores_comp = comp_player.register_results(comp_score)
            comp_high_score = comp_player.high_score(list_of_scores_comp)

            player_score = player.scores()
            list_of_scores_player = player.register_results(player_score)
            player_high_score = player.high_score(list_of_scores_player)

            if comp_high_score > player_high_score:
                print("\nYou Lose!\n")
            elif comp_high_score < player_high_score:
                total_wins += 1
                print("\nYou Win!\n")
            elif comp_high_score == player_high_score:
                print("\nIt's a draw!\n")
            continue
        elif choice == "c":
            old_name = player.name
            player.name = change_name(player.name)
            if player.dic:
                player.dic[player.name] = player.dic.pop(old_name)
            continue
        elif choice == "s":
            print("Total Wins is: " + str(total_wins))
            print(player.get_the_game_resluts())
            print(comp_player.get_the_game_resluts())
            continue
        else:
            print("\nNot a valid choice. Please enter either "
                  "\"p\" or \"s\" or \"c\" or \"r\" or \"q\"")
            continue


def multi_player_game():
    """Multiplayer game follows similar logic to the single player game.
        Two name inputs will be received and then set to both player one and two.
        As long as players do not choose restart or quit options, game will continue to be played.
        Players can choose to change name during the game.
        Players can also choose to display scores"""
    player1 = Player()
    player2 = Player()
    player1.name = input("Enter first player name: ")
    player2.name = input("Enter second player name: ")

    while True:
        choice = next_step()
        if choice == "q":
            print("Exit the game..\n")
            break
        elif choice == "r":
            print("Restart The game...\n")
            player1.dic.clear()
            player2.dic.clear()
            continue
        elif choice == "p":
            print("Start the game: \n")
            player1_score = player1.scores()
            list_of_scores_player = player1.register_results(player1_score)
            player1_high_score = player1.high_score(list_of_scores_player)

            player2_score = player2.scores()
            list_of_scores_player2 = player2.register_results(player2_score)
            player2_high_score = player2.high_score(list_of_scores_player2)

            if player2_high_score > player1_high_score:
                print(f"\n{player2.name} win!\n")
            elif player2_high_score < player1_high_score:
                print(f"\n{player1.name} win!\n")
            elif player2_high_score == player1_high_score:
                print("\nIt's a draw!\n")
            continue
        elif choice == "s":
            print(player1.get_the_game_resluts())
            print(player2.get_the_game_resluts())
            continue
        elif choice == "c":
            print("Who wants to change his name?\n")
            rename = input(f"1.{player1.name}  |  2.{player2.name}  :  ")
            while True:
                if rename == "1":
                    old_name = player1.name
                    player1.name = change_name(player1.name)
                    if player1.dic:
                        player1.dic[player1.name] = player1.dic.pop(old_name)
                    break
                elif rename == "2":
                    old_name = player2.name
                    player2.name = change_name(player2.name)
                    if player2.dic:
                        player2.dic[player2.name] = player2.dic.pop(old_name)
                    break
                else:
                    print("\nNot a valid choice.Who wants to change his name?\n")
                    rename = input(f"1.{player1.name}  |  2.{player2.name}  :  ")
        else:
            print("\nNot a valid choice. Please enter either \"n\" or \"r\" or \"q\"")
            continue


if __name__ == '__main__':
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
            multi_player_game()
            break
        elif game_type == "s":
            print("Single-player mode selected.")
            print()
            single_player_game()
            break
        else:
            print("Not a valid choice. Please enter either \"s\" or \"m\"")
