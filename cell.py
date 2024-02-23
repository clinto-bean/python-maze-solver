from graphics import Line, Point

class Cell:
    
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
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
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, target, undo=False):
        if self._win is None:
            return
        def center(a,b):
            return (a + b)/2
        self.x_center = center(self._x1,self._x2)
        self.y_center = center(self._y1,self._y2)
        target.x_center = center(target._x1,target._x2)
        target.y_center = center(target._y1,target._y2)
        fill_color = "Red"
        if undo:
            fill_color = "Gray"

        # movement methods
        # left
        if self._x1 > target._x1:
            line = Line(Point(self._x1,self.y_center), Point(self._x1, self.y_center))
            self._win.draw_line(line, fill_color)
            line = Line(Point(target.x_center,target.y_center),Point(target._x2,target.y_center))
            self._win.draw_line(line, fill_color)

        # right
        elif self._x1 < target._x1:
            line = Line(Point(self.x_center,self.y_center),Point(self._x2,self.y_center))
            self._win.draw_line(line, fill_color)
            line = Line(Point(target._x1, target.y_center), Point(target.x_center, target.y_center))

        #up
        elif self._y1 > target._y1:
            line = Line(Point(self.x_center,self.y_center),Point(self.x_center, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(target.x_center, target._y2), Point(target.x_center, target.y_center))
            self._win.draw_line(line, fill_color)

        #down
        elif self._y1 < target._y1:
            line = Line(Point(self.x_center, self.y_center), Point(self.x_center, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(target.x_center, target.y_center), Point(target.x_center, target._y1))
            self._win.draw_line(line, fill_color)