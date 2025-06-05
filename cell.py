from graphics import *
from cell import *

class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self,x1 ,y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        start_half_len = abs(self.__x2 - self.__x1) // 2
        start_x_center = self.__x1 + start_half_len
        start_y_center = self.__y1 + start_half_len

        end_half_len = abs(to_cell.__x2 - to_cell.__x1) // 2
        end_x_center = to_cell.__x1 + end_half_len
        end_y_center = to_cell.__y1 + end_half_len

        start = Point(start_x_center, start_y_center)
        end = Point(end_x_center,end_y_center)
        
        line = Line(start, end)
        self.__win.draw_line(line, color)