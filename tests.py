import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_entrance_exit(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(
            m1.cells[0][0].has_top_wall) 
        self.assertFalse(
            m1.cells[num_cols - 1][num_rows - 1].has_bottom_wall) 

    def test_maze_reset_cells_visited(self):
        num_cols = 4 
        num_rows = 3 
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.reset_cells_visited()
        for col in m1.cells:
            for cell in col:
                self.assertFalse(cell.visited)
        #for i in range(self.num_rows):
        #    for j in range(self.num_cols):
        #        self.assertFalse(m1.cells[i][j])

if __name__ == "__main__":
    unittest.main()
