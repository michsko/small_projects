player_1 = ""
player_2 = ""
player_1_all_moves = []
player_2_all_moves = []
player_1_score = 3
player_2_score = 3
winner = False
scored = False
moves = 0
play_ground = {11: "___ ", 12: "___ ", 13: "___ ",
               21: "___ ", 22: "___ ", 23: "___ ",
               31: "___ ", 32: "___ ", 33: "___ ",
               }
def intro():
    global player_1
    global player_2
    print("Welcome to the Tic Tac Toe game. ")
    ''' define players'''
    player_1 = input("Now you insert a name of the player 1: ")
    print(f"Your name is.... {player_1} .... and your symbol is ..... X ......")
    player_2 = input("Now you insert a name of the player 2: ")
    print(f"Your name is.... {player_2} .... and your symbol is ..... O ......")

def player_1_move():
    """ Define moves """
    global moves
    p_1_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    if p_1_move not in play_ground.keys() or p_1_move in player_2_all_moves:
        print("Sorry your choice is not possible. Try again.")
        p_1_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    else:
        pass

    play_ground[p_1_move] = "_X_ "
    print_ground()
    moves += 1


def player_2_move():
    global moves
    p_2_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    if p_2_move not in play_ground.keys() or p_2_move in player_1_all_moves:
        print("Sorry your choice is not possible. Try again.")
        p_2_move = int(input(f"\nPlease insert your move in format row column eg. (row 1 column 1 insert 11)  : "))
    else:
        pass

    play_ground[p_2_move] = "_O_ "
    moves += 1
    print_ground()



def print_ground():
    """method that printing ground """
    print(play_ground[11], play_ground[12], play_ground[13])
    print(play_ground[21], play_ground[22], play_ground[23])
    print(play_ground[31], play_ground[32], play_ground[33])


def check_winner():
    """Define checking the winner"""
    global winner
    player_1_scored = False
    player_2_scored = False
    global player_1_score
    global player_2_score
    global scored
    global player_1
    global player_2
    global play_ground
    global moves

    if play_ground[11] == play_ground[12] == play_ground[13] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[11] == play_ground[12] == play_ground[13] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[21] == play_ground[22] == play_ground[23] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[21] == play_ground[22] == play_ground[23] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[31] == play_ground[32] == play_ground[33] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[31] == play_ground[32] == play_ground[33] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[12] == play_ground[22] == play_ground[32] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[12] == play_ground[22] == play_ground[32] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[13] == play_ground[23] == play_ground[33] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[13] == play_ground[23] == play_ground[33] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[11] == play_ground[21] == play_ground[31] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[11] == play_ground[21] == play_ground[31] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[11] == play_ground[22] == play_ground[33] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[11] == play_ground[22] == play_ground[33] == "_O_ ":
        player_2_score += 1
        player_2_scored = True

    elif play_ground[13] == play_ground[22] == play_ground[31] == "_X_ ":
        player_1_score += 1
        player_1_scored = True

    elif play_ground[13] == play_ground[22] == play_ground[31] == "_0_ ":
        player_2_score += 1
        player_2_scored = True
    else:
        pass

    if player_1_scored:
        print(f"Player {player_1} scored.")
        print(f"Score is {player_1} : {player_1_score}")
        print(f"Score is {player_2} : {player_2_score}")
        scored = True
        play_ground = {11: "___ ", 12: "___ ", 13: "___ ",
                       21: "___ ", 22: "___ ", 23: "___ ",
                       31: "___ ", 32: "___ ", 33: "___ ",
                       }
        moves = 0

    elif player_2_scored:
        print(f"Player {player_2} scored.")
        print(f"Score {player_1} : {player_1_score}")
        print(f"Score {player_2} : {player_2_score}")
        player_2_score += 1
        scored = True
        play_ground = {11: "___ ", 12: "___ ", 13: "___ ",
                       21: "___ ", 22: "___ ", 23: "___ ",
                       31: "___ ", 32: "___ ", 33: "___ ",
                       }
        moves = 0
    elif player_2_score == 5:
        print(f"Winner of the match is {player_2}")
        winner = True
    elif player_1_score == 5:
        print(f"Winner of the match is {player_1}")
        winner = True

    else:
        pass

""" Play """
intro()
print_ground()
while not winner:
    if moves < 9 or not scored:
        player_1_move()
        check_winner()

        player_2_move()
        check_winner()
    elif moves == 9:
        print("this is drew")
        break





