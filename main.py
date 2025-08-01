from graphics import *
from cell import *
from maze import *


def main():
    win_width = 800
    win_height = 600

    win = Window(win_width, win_height)

    maze_width = 10
    maze_height = 10
    maze_num_col = 15
    maze_num_row = 15
    maze_scale = 25

    Maze(maze_width, maze_height, maze_num_row, maze_num_col, maze_scale, maze_scale, win=win)
    win.wait_for_close()


if __name__ == "__main__":
    main()