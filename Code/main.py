from player import Player
from dice import Dice

print("        PIG (Dice Game)        ")
print("-----------------------------------------")
print("Welcome to PIG. This is a dice game of chance.")
print("You can roll the dice 5 times. The highest total number wins\n")

dice = Dice()


def game_type_choice():
    print("Enter \"s\" for single-player mode.")
    print("Enter \"m\" for multi-player mode.")
    game_type = ""

    while game_type != "m" or game_type != "s":
        game_type = input("Make choice: ").lower()
        if game_type == "m":
            print("Multi-player mode selected.")
            print()
            break
        elif game_type == "s":
            print("Single-player mode selected.")
            print()
            break
        else:
            print("Not a valid choice. Please enter either \"s\" or \"m\"")

    return game_type


def game_mode_choice():
    print("Enter \"1\" for Easy mode.")
    print("Enter \"2\" for Medium mode.")
    print("Enter \"3\" for Hard mode.")
    game_mode = ""
    while game_mode != "1" or game_mode != "2" or game_mode != "3":
        game_mode = input("Make choice: ").lower()
        if game_mode == "1":
            print("Easy mode selected.")
            print()
            break
        elif game_mode == "2":
            print("Medium mode selected.")
            print()
            break

        elif game_mode == "3":
            print("Hard mode selected.")
            print()
            break
        else:
            print("Not a valid choice. Please enter either \"1\" or \"2\" or \"3\"")
            game_mode = input("Make choice: ").lower()

    return game_mode


def change_name(current_name):
    print("Do you want to change player name?")
    print("Enter \"y\" for yes.")
    print("Enter \"n\" for no.")
    change_choice = ""

    while change_choice != "y" or change_choice != "n":
        change_choice = input("Make choice: ").lower()
        if change_choice == "y":
            name = input("Ok. Enter new name: ")
            print()
            return name
        elif change_choice == "n":
            name = current_name
            print()
            return name

        else:
            print("Not a valid choice. Please enter either \"y\" or \"n\".")
            change_choice = input("Make choice: ").lower()


def chosen_mode(player):
    global roll_comp, next_choice
    my_game_mode = game_mode_choice()

    print("Enter \"n\" for next roll.")
    print("Enter \"r\" to restart the game.")
    print("Enter \"q\" to quit.")
    next_choice = input("Make choice: ").lower()

    while next_choice != "n" or next_choice != "r" or next_choice != "q":
        if next_choice == "n" or next_choice == "r" or next_choice == "q":
            break
        print("\nNot a valid choice. Please enter either \"n\" or \"r\" or \"q\"")
        next_choice = input("Make choice: ").lower()

    if next_choice == "n":
        s = player.scores()
        total = sum(s)
        comp_count = 0
        comp_list = []
        print("\nYou rolled 5 times.")
        print("Results: " + str(s) + " | Total: " + str(total))

        for index in range(5):
            if my_game_mode == "1":
                roll_comp = dice.roll_easy()
            elif my_game_mode == "2":
                roll_comp = dice.roll_medium()
            elif my_game_mode == "3":
                roll_comp = dice.roll_hard()
            comp_count += roll_comp
            comp_list.append(roll_comp)
        print("\nComputer rolled 5 times.")
        print("Results: " + str(comp_list) + " | Total: " + str(comp_count))

        if comp_count > total:
            print("\nYou Lose!\n")
        elif comp_count < total:
            print("\nYou Win!\n")
        elif comp_count == total:
            print("\nIt's a draw!\n")

        return s
    elif next_choice == "r":
        print()
        print("You have decided to restart the game. You lose!")
        return "r"
    else:
        print()
        print("You have quit the game.")
        return "q"




def multi_player_choice(player):

    print()
    print("It's " + player.name + "'s turn:")
    print("Enter \"n\" for next roll.")
    print("Enter \"r\" to restart the game.")
    print("Enter \"q\" to quit.")
    next_choice = input("Make choice: ").lower()

    while next_choice != "n" or next_choice != "r" or next_choice != "q":
        if next_choice == "n" or next_choice == "r" or next_choice == "q":
            break
        print()
        print("Not a valid choice. Please enter either \"n\" or \"r\" or \"q\"")
        next_choice = input("Make choice: ").lower()

    if next_choice == "n":
        roll = dice.roll_player()
        print()
        print("Rolling the dice, you rolled a {}".format(roll))
        return roll

    elif next_choice == "r":
        print()
        print(player.name + " has restarted the game. " + player.name + " loses!")
        return "r"

    else:
        print()
        print(player.name + " has quit the game. " + player.name + " loses!")
        return "q"


def single_player_game():
    name = input("Choose a player name: ")
    player = Player()
    player.name = name
    result = chosen_mode(player)
    while result != "q":
        if result == "r" or result == "q":
            break
        else:

            j = player.register_results(result)
            player.change_the_name(name)
            print(j)
            print(player.dic)
            result = chosen_mode(player)

    if result == "q":
        print("You will now exit the game.\n")
        return "q"
    else:
        name = change_name(name)
        player.change_the_name(name)
        print(player.dic)
        print("New game is starting....\n")
        return player.dic[name]


def multi_player_game():
    name1 = input("Enter player one name: ")
    name2 = input("Enter player two name: ")
    player1 = Player()
    player2 = Player()
    player1.name = name1
    player2.name = name2

    while True:
                

    while result != "q":
        if result == "r" or result == "q":
            break
        else:

            j = player.register_results(result)
            player.change_the_name(name)
            print(j)
            print(player.dic)
            result = chosen_mode(player)

    if result == "q":
        print("You will now exit the game.\n")
        return "q"
    else:
        name = change_name(name)
        player.change_the_name(name)
        print(player.dic)
        print("New game is starting....\n")
        return [player1.dic[name1], player2.dic[name2]]



    total_score1 = 0
    total_score2 = 0
    p1_rolls = 0
    p2_rolls = 0
    player1 = Player(name1, total_score1)
    player2 = Player(name2, total_score2)

    for index in range(5):
        new_roll = multi_player_choice(player1)
        if new_roll == "r" or new_roll == "q":
            break
        else:
            total_score1 += new_roll
            p1_rolls += 1

        new_roll = multi_player_choice(player2)
        if new_roll == "r" or new_roll == "q":
            break
        else:
            total_score2 += new_roll
            p2_rolls += 1

    player1.total_score = total_score1
    player2.total_score = total_score2

    if new_roll != "r" and new_roll != "q":
        if player1.total_score > player2.total_score:
            print()
            print(player1.name + " wins! Total is: " + str(total_score1))
            print(player2.name + ": " + str(total_score2))
        elif player1.total_score < player2.total_score:
            print()
            print(player2.name + " wins! Total is: " + str(total_score2))
            print(player1.name + ": " + str(total_score1))
        elif player1.total_score == player2.total_score:
            print()
            print("It's a tie.")
            print(player1.name + ": " + str(total_score1))
            print(player2.name + ": " + str(total_score2))
        return [player1, player2]
    elif new_roll == "r":
        return "r"
    elif new_roll == "q":
        return "q"


the_game_type = game_type_choice()
if the_game_type == "s":
    single_player_game()
else:
    multi_player_game()
