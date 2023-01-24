from random import randint

# This creates the board/grid with the append method
def get_sea():
    sea = []
    for _ in range(8):
        sea.append(["¤"] * 8)
    return sea

# This function prints the board
def print_sea(sea):
    for row in sea:
        print((" ").join(row))
print(" ")



# This function helps the player to position their ship on the grid, the ship will be marked as "@".
def get_player_ship_location():
    valid_ship_row = False
    valid_ship_col = False
    print(("*********Write down your wished coordinates*********\nEnter a number between 1 - {}").format(len(sea)))
    while valid_ship_row == False:
        try: 
            player_ship_row = int(
                input("Enter row to place your ship: "))
            if (player_ship_row not in range(1, len(sea) + 1)):
                 print("Not a valid request, you must enter a number between 1 - {}".format(len(sea) + 1))
                else:
                    valid_ship_row = True
                except ValueError:
                    print("Not a valid request, have another try!")
                while valid_ship_col == False:
                    try:
                        player_ship_col = int(
                            input("Enter a column where you want to plave your ship: "))
                        print(" ")
                        if (player_ship_col not in range(1, len(sea) + 1)):
                            print("This is not a valid column, you must enter a number between 1-{}"format(len(sea) + 1))
                        else:
                            sea[player_ship_row - 1][player_ship_col - 1] = "@"
                            valid_ship_col = True
                        except ValueError:
                            print("This is not a valid number, have another try!")
            return sea


def random_row():

def random_col():

def get_enemy_ships

