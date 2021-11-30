import unittest
import bfs


class TestBfs(unittest.TestCase):
    def test_mat(self):
        res = bfs.matrix_to_list(bfs.g)  # this function converts a list into dict
        self.assertIsInstance(res, dict)

    def test_bfs(self):
        val = bfs.bfs(bfs.gr, bfs.given_num)  # this function takes in a empty list and add the bf searched elements
        self.assertTrue(val)

    def test_inputList(self):
        self.assertTrue(bfs.inputs_list)  # testing whether the files from the provided folder and importing or not


if __name__ == '__main__':
    unittest.main()