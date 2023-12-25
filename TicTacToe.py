from __future__ import print_function
from human_player import HumanPlayer
from ai_player import AIPlayer

board= [
    [' . ',' . ',' . '],
    [' . ',' . ',' . '],
    [' . ',' . ',' . ']
]

players = [HumanPlayer('X'), AIPlayer('0')]
current_player= 0

def play(board,next_move):
    global current_player
    row,column=next_move
    player_value=players[current_player].value
    board[row][column]=player_value
    current_player = (current_player + 1) % len(players)
    print_board(board)

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("{:^3}".format(board[i][j]), end='')
        print("")


def is_valid(board,next_move):
    row,column=next_move
    return board[row][column]== ' . '


def _is_all_the_same(board,i1,i2,i3,val):
    if (board[i1[0]][i1[1]] == board[i2[0]][i2[1]] and 
       board[i1[0]][i1[1]] == board[i3[0]][i3[1]] and
       board[i1[0]][i1[1]] == val):
       return True


def get_winner(board):
    for player in ['X', '0']:
        if _is_all_the_same(board,(0,0),(0,1),(0,2),player): return player
        if _is_all_the_same(board,(1,0),(1,1),(1,2),player): return player
        if _is_all_the_same(board,(2,0),(2,1),(2,2),player): return player

        if _is_all_the_same(board,(0,0),(1,0),(2,0),player): return player
        if _is_all_the_same(board,(0,1),(1,1),(2,1),player): return player
        if _is_all_the_same(board,(0,2),(1,2),(2,2),player): return player

        if _is_all_the_same(board,(0,0),(1,1),(2,2),player): return player
        if _is_all_the_same(board,(0,2),(1,1),(2,0),player): return player
    

def game_over(board):
    if get_winner(board) is not None:
        return True
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' . ':
                return False
    return True


while not game_over(board):
    next_move=players[current_player].get_move()
    if is_valid(board,next_move):
        play(board,next_move)


winner=get_winner(board)
print("Yay! " +winner+ " won!!")

