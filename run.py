from random import randint


def make_sea():
    sea = []
  for _ in range(8):
    sea.append(["¤"] * 8)
    return sea

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