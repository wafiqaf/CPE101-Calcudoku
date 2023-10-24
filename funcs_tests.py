import unittest

import solver_funcs


class TestCases(unittest.TestCase):
    def test_check_valid_with_finished_puzzle(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_valid(puzzle, cages))

    def test_check_valid_with_finished_puzzle17(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [4, 3, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_valid(puzzle, cages))

    def test_check_valid_with_finished_puzzle2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 3, 4, 3, 2],
                  [2, 3, 3, 4, 1],
                  [3, 1, 2, 2, 5],
                  [5, 1, 3, 2, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_valid(puzzle, cages))

    def test_check_row1(self):
        puzzle = [[2, 2, 3, 4],
                  [1, 2, 3, 4],
                  [4, 5, 3, 6]]
        self.assertFalse(solver_funcs.check_rows_valid(puzzle))

    def test_check_row2(self):
        puzzle = [[2, 1, 3, 4],
                  [1, 2, 3, 4],
                  [4, 5, 3, 6]]
        self.assertTrue(solver_funcs.check_rows_valid(puzzle))

    def test_check_onerow1(self):
        cage = [2, 1, 3, 4]
        self.assertTrue(solver_funcs.check_one_row(cage))

    def test_check_onerow2(self):
        cage = [5, 2, 0, 5]
        self.assertFalse(solver_funcs.check_one_row(cage))

    def test_check_onerow3(self):
        cage = [0, 0, 2, 3]
        self.assertTrue(solver_funcs.check_one_row(cage))

    def test_check_onecol1(self):
        puzzle = [2, 1, 3, 4, 4]
        self.assertFalse(solver_funcs.check_one_col(puzzle))

    def test_check_onecol2(self):
        puzzle = [2, 1, 3, 4, 5]
        self.assertTrue(solver_funcs.check_one_col(puzzle))

    def test_check_onecol3(self):
        puzzle = [0, 0, 2, 3, 4]
        self.assertTrue(solver_funcs.check_one_col(puzzle))

    def test_check_colmns1(self):
        puzzle = [[2, 1, 3, 4, 5],
                  [1, 2, 3, 4, 2],
                  [4, 5, 3, 6, 2],
                  [2, 3, 4, 2, 4],
                  [2, 3, 4, 5, 4]]
        self.assertFalse(solver_funcs.check_columns_valid(puzzle))

    def test_check_colmns2(self):
        puzzle = [[2, 1, 3, 4, 5],
                  [1, 2, 2, 1, 2],
                  [4, 5, 1, 6, 1],
                  [5, 3, 4, 5, 4],
                  [3, 4, 5, 2, 3]]
        self.assertTrue(solver_funcs.check_columns_valid(puzzle))

    def test_check_one_cage1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cage = [5, 2, 0, 5]
        self.assertTrue(solver_funcs.check_one_cage(cage, puzzle))

    def test_check_one_cage2(self):
        puzzle = [[4, 1, 3, 5, 2],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cage = [8, 3, 1, 2, 6]
        self.assertFalse(solver_funcs.check_one_cage(cage, puzzle))

    def test_check_one_cage3(self):
        puzzle = [[4, 1, 3, 5, 2],
                  [1, 0, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cage = [8, 3, 1, 2, 6]
        self.assertTrue(solver_funcs.check_one_cage(cage, puzzle))

    def test_check_cages_valid1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cages_valid2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 2, 2, 6],
                 [8, 2, 1, 3],
                 [6, 2, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 3, 15],
                 [14, 4, 4, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_cages_valid(puzzle, cages))


if __name__ == '__main__':
    unittest.main()
