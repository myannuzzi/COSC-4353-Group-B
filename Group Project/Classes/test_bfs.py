import unittest
import bfs


class TestBfs(unittest.TestCase):
    def test_mat(self):
        m = [[0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
        out = {0: [1, 2, 4], 1: [0, 3], 2: [0, 3], 3: [1, 2, 5], 4: [0, 5], 5: [3, 4]}
        res = bfs.matrix_to_list(m)  # this function converts a list into dict
        self.assertIsInstance(res, dict)
        self.assertEqual(res, out)

    def test_bfs(self):
        g = {0: [1, 2, 4], 1: [0, 3], 2: [0, 3], 3: [1, 2, 5], 4: [0, 5], 5: [3, 4]}
        out = [2, 0, 3, 1, 4, 5]
        val = bfs.bfs(g, 2)  # this function takes in a empty list and add the bf searched elements
        self.assertTrue(val)
        self.assertEqual(val, out)

    def test_inputList(self):
        self.assertTrue(bfs.inputs_list)  # testing whether the files from the provided folder and importing or not


if __name__ == '__main__':
    unittest.main()
