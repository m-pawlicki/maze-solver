from time import sleep
from graphics import *
from cell import *

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        #fill in _cells, 2d list of Cells
        pass

    def __draw_cell(self, i, j):
        #calculate x/y posi of cell based on i/j pos + cell size
        Cell.draw()
        self.__animate()

    def __animate(self):
        self.win.redraw()
        sleep(0.05)