from random import randint

player_ships = [['']*8 for x in range(8)]
player_guess = [['']*8 for x in range(8)]
computer_ships = [['']*8 for x in range(8)]
computer_guess = [['']*8 for x in range(8)]

let_to_num ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    #Enter a row 1-8
    row=input('Please write a row 1-8 ').upper()
    while row not in '12345678':
        print("Please write down valid row! ")
        row=input('Enter a ship row 1-8 ')
    #Enter a column A-H
    column=input('Enter a ship column A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Please write down a valid column! ")
        column=input('Enter a ship column A-H! ')
    return int(row)-1,let_to_num[column]

def create_ships():
    pass

def count_sunk_ships():
    pass