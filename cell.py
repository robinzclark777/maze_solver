from graphics import Line, Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self._x1 = None 
        self._x2 = None 
        self._y1 = None 
        self._y2 = None 
        self.visited = False
        self.end_cell = False
        self.begin_cell = False
        self.loser_cell = False


    def printcell(self, desc):
        print(f"for {desc} ...x1 is {self._x1} y1 is {self._y1} x2 is {self._x2} y2 is {self._y2}")

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")


    def draw_move(self, to_cell, undo=False):
        x1 = self._x1 + (self._x2 - self._x1) // 2
        y1 = self._y1 + (self._y2 - self._y1) // 2
        x2 = to_cell._x1 + (to_cell._x2 - to_cell._x1) // 2
        y2 = to_cell._y1 + (to_cell._y2 - to_cell._y1) // 2
        if undo:
            line = Line(Point(x1, y1), Point(x2, y2))
            self._win.draw_line(line, "gray")
        else:
            line = Line(Point(x1, y1), Point(x2, y2))
            self._win.draw_line(line, "red")
        
        
