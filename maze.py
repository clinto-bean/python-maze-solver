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
        current = self[i,j]
        current.visited = True
        while True:

            unvisited = []

            #choosing who to visit

            if j > 0 and not self._cells[i][j-1].visited:
                neighbor = self[i, j-1]
                if neighbor.visited is False:
                    unvisited.append(neighbor)
                
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                neighbor = self[i, j+1]
                if neighbor.visited is False:
                    unvisited.append(neighbor)
                    
            if i > 0 and not self._cells[i - 1][j].visited:
                    neighbor = self[i-1,j]
                    if neighbor.visited is False:
                        unvisited.append(neighbor)

            if i < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbor = self[i+1,j]
                if neighbor.visited is False:
                    unvisited.append(neighbor)

            if len(unvisited) == 0:
                break
            
            new_cell = random.choice(unvisited)

            if new_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if new_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if new_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if new_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                
            neighbor_index = random.randrange(len(unvisited))
            neighbor = unvisited[neighbor_index]

            if neighbor[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                
            if neighbor[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
                        
            if neighbor[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if neighbor[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(neighbor[0], neighbor[1])
            self._reset_cells_visited()

    def _reset_cells_visited(self):
        for cell in self._cells:
            cell.visited = False

    def _solve(self, i=0, j=0):
        self._solve_r(i, j)

    def _solve_r(self, i, j):
        current = self[i, j]

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

    
