from graphics import *
from cell import *
from maze import *


def main():
    win = Window(800, 600)
    maze = Maze(2, 2, 10, 10, 50, 50, win=win)
    win.wait_for_close()


if __name__ == "__main__":
    main()