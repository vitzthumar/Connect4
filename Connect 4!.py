# Connect 4! Made by August Vitzthum
import intrographics

window = intrographics.window(850, 850)
background = window.image(0, 0, "Connect 4! Grid.gif")

# Nonlocal variables
tile_count, location = 0, 745
turn = "red"

# Creating red and blue arrows
def make_red():
    global red_arrow
    red_arrow = window.image(385, 23, "Red Arrow.gif")
    red_arrow.group("arrow")

def make_blue():
    global blue_arrow
    blue_arrow = window.image(385, 23, "Blue Arrow.gif")
    blue_arrow.group("arrow")

def fill_red(location):
    red_tile = window.image(red_arrow.x, location, "Red Tile.gif")
    red_tile.group("tile")
    red_tile.group("red")
    red_tile.group("removable")

def fill_blue(location):
    blue_tile = window.image(blue_arrow.x, location, "Blue Tile.gif")
    blue_tile.group("tile")
    blue_tile.group("blue")
    blue_tile.group("removable")

def remove_arrow():
    for arrow in window.all("arrow"):
        window.remove(arrow)
        arrow.ungroup("arrow")

def check(color):
    global south_count, east_count, south_east_count, north_east_count
    south_count, east_count, south_east_count, north_east_count = 0, 0, 0, 0

    for tile in window.all(color):
        for other_tile in window.all(color):

            if tile.x == other_tile.x and tile.y == other_tile.y - 120:

                for other_tile in window.all(color):

                    if tile.x == other_tile.x and tile.y == other_tile.y - 240:

                        for other_tile in window.all(color):

                            if tile.x == other_tile.x and tile.y == other_tile.y - 360:

                                south_count = 3

    for tile in window.all(color):
        for other_tile in window.all(color):


            if tile.x == other_tile.x + 120 and tile.y == other_tile.y - 120:

                for other_tile in window.all(color):

                    if tile.x == other_tile.x + 240 and tile.y == other_tile.y - 240:

                        for other_tile in window.all(color):

                            if tile.x == other_tile.x + 360 and tile.y == other_tile.y - 360:

                                north_east_count = 3

    for tile in window.all(color):
        for other_tile in window.all(color):

            if tile.x == other_tile.x + 120 and tile.y == other_tile.y:

                for other_tile in window.all(color):

                    if tile.x == other_tile.x + 240 and tile.y == other_tile.y:

                        for other_tile in window.all(color):

                            if tile.x == other_tile.x + 360 and tile.y == other_tile.y:

                                east_count = 3

    for tile in window.all(color):
        for other_tile in window.all(color):

            if tile.x == other_tile.x + 120 and tile.y == other_tile.y + 120:

                for other_tile in window.all(color):

                    if tile.x == other_tile.x + 240 and tile.y == other_tile.y + 240:

                        for other_tile in window.all(color):

                            if tile.x == other_tile.x + 360 and tile.y == other_tile.y + 360:

                                 south_east_count = 3

def move_arrow(key):
    global turn, tile_count, x_coord, y_coord

    for arrow in window.all("arrow"):
        if key == "Right":
            if arrow.x != 745:
                arrow.move(120, 0)
        if key == "Left":
            if arrow.x != 25:
                arrow.move(-120, 0)

        if key == "Return":
            tile_count = 1
            overall_count = 0

            for tile in window.all("tile"):

                if tile.x == arrow.x:
                    tile_count += 1
            if tile_count != 7:
                location = 865 - (tile_count * 120)
                y_coord = location
                x_coord = arrow.x

                if turn == "blue":
                    remove_arrow()
                    make_red()
                    fill_blue(location)
                    check("blue")
                    if south_count == 3 or east_count == 3 or south_east_count == 3 or north_east_count == 3:
                        end_board = window.image(0, 0, "End Board.gif")
                        end_board.group("removable")
                        blue_wins = window.image(50, 295, "Blue Wins!.gif")
                        blue_wins.group("removable")
                        window.offKeyPress(move_arrow)
                        window.onKeyPress(restart)
                    turn = "red"

                elif turn == "red":
                    remove_arrow()
                    make_blue()
                    fill_red(location)
                    check("red")
                    if south_count == 3 or east_count == 3 or south_east_count == 3 or north_east_count == 3:
                        end_board = window.image(0, 0, "End Board.gif")
                        end_board.group("removable")
                        red_wins = window.image(50, 295, "Red Wins!.gif")
                        red_wins.group("removable")
                        window.offKeyPress(move_arrow)
                        window.onKeyPress(restart)
                    turn = "blue"

            for tile in window.all("tile"):
                overall_count += 1
                if overall_count == 42:
                    tie_game = window.image(50, 295, "Tie Game!.gif")
                    tie_game.group("removable")
                    end_board = window.image(0, 0, "End Board.gif")
                    end_board.group("removable")
                    window.offKeyPress(move_arrow)
                    window.onKeyPress(restart)

def restart(key):
    if key == "space":
        for shape in window.all("removable"):
            window.remove(shape)
            window.onKeyPress(move_arrow)
            window.offKeyPress(restart)
    if key == "Escape":
        window.close()

window.onKeyPress(move_arrow)

make_red()

window.open()




