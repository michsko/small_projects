print("Welcome to the Tic Tac Toe game. ")

''' define players and score '''

player_1 = input("Now you insert a name of the player 1: ")
print(f"Your name is.... {player_1} .... and your symbol is ..... x ......")
player_2 = input("Now you insert a name of the player 2: ")
print(f"Your name is.... {player_2} .... and your symbol is ..... o ......")

player_1_score = 0
player_2_score = 0

score = f" the score of your play is player 1 {player_1_score} : player 2 {player_2_score}"


""" Define moves of players"""

player_1_all_moves = []
player_2_all_moves = []

""" Create play-ground """
play_ground = {11: "___ ", 12: "___ ", 13: "___ ",
               21: "___ ", 22: "___ ", 23: "___ ",
               31: "___ ", 32: "___ ", 33: "___ ",
               }


def print_ground():
    """method that printing ground """
    print(play_ground[11], play_ground[12], play_ground[13])
    print(play_ground[21], play_ground[22], play_ground[23])
    print(play_ground[31], play_ground[32], play_ground[33])

""" Play """

winner = False
moves = 0
print_ground()
while not winner:
    if moves < 9:
        player_1_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
        player_1_all_moves.append(player_1_move)
        play_ground[player_1_move] = "_X_ "
        moves += 1

        print_ground()

        player_2_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
        player_2_all_moves.append(player_2_move)
        play_ground[player_2_move] = "_O_ "
        moves += 1

        print_ground()


