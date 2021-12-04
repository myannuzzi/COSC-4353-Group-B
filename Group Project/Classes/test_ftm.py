import unittest
import file_to_mat as ftm
import bfs
import minimizeFeature as mf


class TestFtm(unittest.TestCase):
    def test_ftm_mf(self):  # to test whether the file input is being converted into an adjacency matrix
        res = ftm.file_to_matrix(mf.input_folder, mf.given_file)
        self.assertIsInstance(res, list)

    def test_ftm_bfs(self):
        res = ftm.file_to_matrix(bfs.input_folder, bfs.given_file)
        self.assertIsInstance(res, list)

    # def test_range(self):
    #     self.assertRaises(IndexError, ftm.file_to_matrix, bfs.input_folder, -1)


if __name__ == '__main__':
    unittest.main()
