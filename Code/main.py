from re import M, S
from player import Player
from dice import Dice
from AI import AI

def change_name(name):
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
    


def next_step():
    print("\nEnter \"p\" to start the game.")
    print("Enter \"s\" to show the scores.")
    print("Enter \"c\" to change the name.")
    print("Enter \"r\" to restart the game.")
    print("Enter \"q\" to quit.\n")
    choice = input("Make choice: ").lower()
    return choice


def single_player_game():
    comp = AI()
    player = Player()
    comp_player = Player()
    total_wins = 0
    comp_player.name = "computer"
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
            total_wins = 0
            continue
        elif choice == "p":
            print("Start the game: \n")
            comp_score = comp.comp_scores()
            List_of_scores_comp = comp_player.register_results(comp_score)
            comp_high_score = comp_player.highScore(List_of_scores_comp)
        
            player_score = player.scores()
            List_of_scores_player = player.register_results(player_score)
            player_high_score = player.highScore(List_of_scores_player)
            
            if comp_high_score > player_high_score:
                print("\nYou Lose!\n")
            elif comp_high_score < player_high_score:
                total_wins =+ 1
                print("\nYou Win!\n")
            elif comp_high_score == player_high_score:
                print("\nIt's a draw!\n")
            continue
        elif choice == "c":
            old_name = player.name
            player.name = change_name(player.name)
            player.dic[player.name] = player.dic.pop(old_name)
            continue
        elif choice == "s":
            print("Total Wins is: " + str(total_wins))
            print(player.get_the_game_resluts())
            print(comp_player.get_the_game_resluts())
            continue
        else:
            print("\nNot a valid choice. Please enter either \"p\" or \"s\" or \"c\" or \"r\" or \"q\"")
            continue

def multi_player_game():
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
            List_of_scores_player = player1.register_results(player1_score)
            player1_high_score = player1.highScore(List_of_scores_player)

            player2_score = player2.scores()
            List_of_scores_player2 = player2.register_results(player2_score)
            player2_high_score = player2.highScore(List_of_scores_player2)
        
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
            rename = input(f"1.{player1.name}        2.{player2.name}")
            if rename == "1":
                old_name = player1.name
                player1.name = change_name(player1.name)
                player1.dic[player1.name] = player1.dic.pop(old_name)
            else:
                old_name = player2.name
                player2.name = change_name(player2.name)
                player2.dic[player2.name] = player2.dic.pop(old_name)

            continue
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
