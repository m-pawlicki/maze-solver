import random
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
        seed = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed is not None:
            self.__seed = random.seed(seed)

        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.solve()

    def __create_cells(self):
        for i in range(self.__num_cols):
            cols = []
            for j in range(self.__num_rows):
                cols.append(Cell(self.__win))
            self.__cells.append(cols)

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
        self.__animate(0.005)

    def __animate(self, delay=0):
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(delay)
    
    def __break_entrance_and_exit(self):
        # Deletes top and bottom walls from the first and last cell respectively
        entrance: Cell = self.__cells[0][0]
        exit: Cell = self.__cells[self.__num_cols-1][self.__num_rows-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
    
    def __break_walls_r(self, i, j):
        cells = self.__cells
        cells[i][j].visited = True
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while True:
            to_visit = []
            for dx,dy in offsets:
                x = i+dx
                y = j+dy
                if self.__is_valid_cell(x, y):
                    to_visit.append((x, y))
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            # Pick a random cell from the list of adjacent ones
            choice = to_visit[random.randrange(len(to_visit))]
            # Delete the shared wall
            match self.__check_wall_side(i, j, choice[0], choice[1]):
                case "top":
                    cells[i][j].has_top_wall = False
                    cells[choice[0]][choice[1]].has_bottom_wall = False
                case "bottom":
                    cells[i][j].has_bottom_wall = False
                    cells[choice[0]][choice[1]].has_top_wall = False
                case "left":
                    cells[i][j].has_left_wall = False
                    cells[choice[0]][choice[1]].has_right_wall = False
                case "right":
                    cells[i][j].has_right_wall = False
                    cells[choice[0]][choice[1]].has_left_wall = False
                case _:
                    return
            self.__break_walls_r(choice[0], choice[1])


    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def __is_valid_cell(self, i, j):
        cells = self.__cells
        # Checking if out of bounds or if has been visited already
        if i < 0 or j < 0 or i >= self.__num_cols or j >= self.__num_rows or cells[i][j].visited is True:
            return False
        return True
    
    def __check_wall_side(self, i, j, dx, dy):
        # Left
        if dx == i - 1:
            return "left"
        # Right
        if dx == i + 1:
            return "right"
        # Up
        if dy == j - 1:
            return "top"
        # Down
        if dy == j + 1:
            return "bottom"
        
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self.__animate()
        # goal cell
        max_col = self.__num_cols-1
        max_row = self.__num_rows-1
        goal_cell: Cell = self.__cells[max_col][max_row]
        # current cell
        current_cell: Cell= self.__cells[i][j]
        current_cell.visited = True
        if current_cell == goal_cell:
            return True
        # checking around current cell
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx,dy in offsets:
            x = i+dx
            y = j+dy
            direction = self.__check_wall_side(i, j, x, y)
            # checking if it's in bounds and not visited yet
            if self.__is_valid_cell(x, y):
                next_cell: Cell = self.__cells[x][y]
                # checking if there's no wall
                wall = getattr(current_cell, f"has_{direction}_wall")
                if wall is False:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(x, y):
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo=True)
        return False