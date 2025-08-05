from graphics import *
from cell import *
from maze import *


def main():
    win_width = 800
    win_height = 600

    win = Window(win_width, win_height)

    maze_width = 5
    maze_height = 5
    maze_num_col = 25
    maze_num_row = 15
    maze_scale = 30

    Maze(maze_width, maze_height, maze_num_row, maze_num_col, maze_scale, maze_scale, win=win)
    win.wait_for_close()


if __name__ == "__main__":
    main()