from graphics import Window
from maze import Maze


def main():
    num_rows = 13  
    num_cols = 25 
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    solved = maze.solve()
    if solved:
        print("found your way out")
    else:
        print("you are stuck in maze")

    win.wait_for_close()


main()
