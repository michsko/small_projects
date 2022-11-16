print("Welcome to the Tic Tac Toe game. ")

''' define players and score '''

player_1 = input("Now you insert a name of the player 1: ")
print(f"Your name is.... {player_1} .... and your symbol is ..... x ......")
player_2 = input("Now you insert a name of the player 2: ")
print(f"Your name is.... {player_2} .... and your symbol is ..... o ......")

player_1_score = 0
player_2_score = 0
winner = False
scored = False
moves = 0
score = f"The score of your play is {player_1} {player_1_score} : {player_2_score} {player_2}"


""" Define moves of players"""
player_1_all_moves = []
player_2_all_moves = []


def player_1_move():
    p_1_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    if p_1_move not in play_ground.keys() or p_1_move in player_2_all_moves:
        print("Sorry your choice is not possible. Try again.")
        p_1_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    else:
        pass

    player_1_all_moves.append(p_1_move)
    play_ground[p_1_move] = "_X_ "
    print_ground()


def player_2_move():
    p_2_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    if p_2_move not in play_ground.keys() or p_2_move in player_1_all_moves:
        print("Sorry your choice is not possible. Try again.")
        p_2_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    else:
        pass

    player_2_all_moves.append(p_2_move)
    play_ground[p_2_move] = "_O_ "
    print_ground()



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


def check_winner():
    """Define checking the winner"""
    winning_combinations = [[11, 12, 13], [21, 22, 23], [31, 32, 33], [13, 23, 33],
                           [12, 22, 32], [11, 21, 31], [11, 22, 33], [12, 22, 31]]
    global winner
    global player_1_score
    global player_2_score
    global scored

    if winning_combinations in player_1_all_moves:
        player_1_score += 1
        print(f"Player {player_1} scored.")
        if player_1_score < 5:
            print(score)
            scored = True
        else:
            print(score)
            print(f"Winner of the match is {player_1}")
            winner = True




    elif player_2_all_moves in winning_combinations:
        winner = True
        player_2_score += 1
        print(f"Player {player_2} scored.")
        if player_2_score < 5:
            print(score)
            scored = True
        else:
            print(score)
            print(f"Winner of the match is {player_2}")
            winner = True

    else:
        pass

""" Play """


print_ground()
while not winner:
    if moves <= 9 or not scored:
        player_1_move()
        moves += 1
        check_winner()

        player_2_move()
        moves += 1
        check_winner()
    else:
        break


