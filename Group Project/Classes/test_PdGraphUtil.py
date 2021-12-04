import unittest
from PdGraphUtil import *
import numpy as np
import pandas as pd
import os


class TestGraph(unittest.TestCase):
    def test_df_to_adj_matrix(self):
        df = pd.DataFrame([["A", "B"], ["A", "C"], ["A", "D"], ["A", "D"], ["B", "D"], ["C", "A"],  ["Z", "B"]],
                          columns=["Column1", "Column2"])
        df_adj_mat = df_to_adj_matrix(df.Column1, df.Column2)
        headers = ['A', 'B', 'C', 'D', 'Z']
        expected_adj_mat = np.array([
            [0, 1, 1, 2, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ])
        d_types = {"A": np.int64, "B": np.int64,
                   "C": np.int64, "D": np.int64, "Z": np.int64, }
        expected_df = pd.DataFrame(data=expected_adj_mat,
                                   index=headers,
                                   columns=headers).astype(d_types)
        self.assertTrue(expected_df.equals(df_adj_mat))

    def test_adj_mat_to_df(self):
        headers = ['A', 'B', 'C', 'D', 'Z']
        adj_mat = np.array([
            [0, 1, 1, 2, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ])
        d_types = {"A": np.int64, "B": np.int64,
                   "C": np.int64, "D": np.int64, "Z": np.int64, }
        df_adj_mat = pd.DataFrame(data=adj_mat,
                                  index=headers,
                                  columns=headers).astype(d_types)
        df = adj_mat_to_df(df_adj_mat, ["Column1", "Column2"])
        expected_df = pd.DataFrame([["A", "B"], ["A", "C"], ["A", "D"], ["A", "D"], ["B", "D"], ["C", "A"],  ["Z", "B"]],
                                   columns=["Column1", "Column2"])
        self.assertTrue(expected_df.equals(df))

    def test_get_edgelist_from_graph(self):
        script_dir = os.path.dirname(__file__)
        input_file = script_dir + "/Datasets/graph1list.txt"
        edge_list = get_edgelist_from_graph(input_file)
        expected_list = np.array([[1, 2], [1, 3], [2, 1], [2, 3], [2, 4], [2, 5], [
                                 3, 1], [3, 2], [3, 4], [4, 2], [4, 3], [4, 5], [5, 2], [5, 4]])
        self.assertTrue(np.array_equal(edge_list, expected_list))

    def test_get_adj_mat(self):
        script_dir = os.path.dirname(__file__)
        input_file = script_dir + "/Datasets/graph1list.txt"
        adj_mat = get_adj_mat(input_file)
        expected_adj_mat = np.array([[0, 1, 1, 0, 0], [1, 0, 1, 1, 1], [
                                    1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 1, 0, 1, 0]])
        self.assertTrue(np.array_equal(adj_mat, expected_adj_mat))
        

    def test_csv_to_numpy_adjmat(self):
        script_dir = os.path.dirname(__file__)
        input_file_unweighted = script_dir + "/Datasets/graph1mat.csv"
        adj_mat_unweighted = csv_to_numpy_adjmat(input_file_unweighted)
        expected_unweighted = np.array([[0, 1, 1, 0, 0], [1, 0, 1, 1, 1], [
                                       1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 1, 0, 1, 0]])
        self.assertTrue(np.array_equal(
            adj_mat_unweighted, expected_unweighted))

        input_file_weighted = script_dir + "/Datasets/graph1weightedMat.csv"
        adj_mat_weighted = csv_to_numpy_adjmat(input_file_weighted)
        expected_weighted = np.array([[0, 3, 7, 0, 0], [3, 0, 2, 2, 4], [
                                     1, 2, 0, 1, 0], [0, 2, 1, 0, 10], [0, 4, 0, 10, 0]])
        self.assertTrue(np.array_equal(adj_mat_weighted, expected_weighted))

    def test_adj_mat_to_csv(self):
        script_dir = os.path.dirname(__file__)
        adj_mat = np.array([[0, 1, 1, 0, 0], [1, 0, 1, 1, 1], [
                           1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 1, 0, 1, 0]])
        adj_mat_to_csv(adj_mat, script_dir + "/")
        PATH = script_dir + '/adjMatrix.csv'
        flag = False
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            flag = True

        # check the file exists and return true, which is then checked by the test
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()