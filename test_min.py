import unittest
import pandas
import minimizeFeature as mf


class TestMin(unittest.TestCase):
    def test_nodes(self):
        n = mf.nodes
        self.assertIsInstance(n, int)  # to test whether nodes input is an integer

    def test_edges(self):
        e = mf.edges
        self.assertIsInstance(e, int)  # to test whether edges input is an integer

    def test_inputList(self):
        self.assertTrue(mf.inputs_list)  # testing whether the files from the provided folder and importing or not

    def test_g(self):
        self.assertIsInstance(mf.g, list)  # to check whether the string is being converted into an adjacency matrix

    def test_df(self):
        self.assertIsInstance(mf.df2, pandas.DataFrame)


# commit to feature branch


if __name__ == '__main__':
    unittest.main()
