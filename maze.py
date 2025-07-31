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
        win: Window = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            cols = []
            for j in range(self.__num_rows):
                cols.append(Cell(self.__win))
            self.__cells.append(cols)

        self.__break_entrance_and_exit()

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        #calculate x/y posi of cell based on i/j pos + cell size
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_x
        cell = self.__cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(0.05)
    
    def __break_entrance_and_exit(self):
        entrance: Cell = self.__cells[0][0]
        exit: Cell = self.__cells[self.__num_cols-1][self.__num_rows-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False