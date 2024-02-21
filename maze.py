from cell import Cell
import random
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ): 
        self._cells = []
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y

        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        
    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        exit = self._cells[len(self._cells)-1][len(self._cells[0])-1]
        exit.has_bottom_wall = False

    def _break_walls_r(self, i=0, j=0):
        start = self[i,j]
        current = start

        current.visited = True

        unvisited = []

        if j > 0:
            left = self[i, j-1]
            if left.visited is False:
                unvisited.append(left)
            
        if j < self._num_cols - 1:
            right = self[i, j+1]
            if right.visited is False:
                unvisited.append(right)
            
        if i > 0:
            top = self[i-1,j]
            if top.visited is False:
                unvisited.append(top)

        if i < self._num_rows - 1:
            bottom = self[i+1,j]
            if bottom.visited is False:
                unvisited.append(bottom)

        while len(unvisited) > 0:
            neighbor = random.choice(unvisited)
            # left
            if neighbor.j < current.j:
                current.has_left_wall = False
                neighbor.has_right_wall = False
            #right
            if neighbor.j > current.j:
                current.has_right_wall = False
                neighbor.has_left_wall = False
            #above
            if neighbor.i < current.i:
                current.has_top_wall = False
                neighbor.has_bottom_wall = False
            #below
            if neighbor.i > current.i:
                current.has_bottom_wall = False
                neighbor.has_top_wall = False
            unvisited.remove(neighbor)
            current = neighbor
            self._break_walls_r(current.i, current.j)

    def _draw_cell(self,i,j):
        cell_x1 = i * self._cell_size_x + self._x1
        cell_y1 = j * self._cell_size_y + self._y1
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1,cell_y1,cell_x2,cell_y2)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

    
