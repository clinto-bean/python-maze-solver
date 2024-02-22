import random
import unittest 
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m._cells),
            num_cols,
        )
        self.assertEqual(
            len(m._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 24
        num_rows = 16
        m = Maze(0, 0, num_rows, num_cols, 8, 8)
        self.assertEqual(
            len(m._cells),
            num_cols,
        )
        self.assertEqual(
            len(m._cells[0]),
            num_rows
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m._cells[len(m._cells)-1][len(m._cells[0])-1].has_bottom_wall,
            False
        )

    def test_visiting_cells_and_resetting_visited(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in m._cells:
            random_row = random.choice(m._cells)
            return random_row
        index = random.randint(0, len(random_row))

        self.assertEqual(
            m._cells[random_row[index]].visited,
            False
        )

    

if __name__ == "__main__":
    unittest.main()