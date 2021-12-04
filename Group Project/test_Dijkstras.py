import unittest
from DijkstraShortestPath import *
import numpy as np
import os

class TestGraph(unittest.TestCase):

    def test_dijkstra(self):
        script_dir = os.path.dirname(__file__)  
        input_file1 = script_dir + "/Classes/DataSets/graph1weightedMat.csv"
        shortest_path1 = dijkstra(input_file1, 0)
        expected_path1 = np.array([[0, 1], [0, 1, 2], [0, 1, 3], [0, 1, 4]])
        self.assertTrue(np.array_equal(shortest_path1,expected_path1))

        input_file2 = script_dir + "/Classes/DataSets/graph2weightedMat.csv"
        shortest_path2 = dijkstra(input_file2, 0)
        expected_path2 = np.array([[0, 1], [0, 2], [0, 4, 5, 3], [0, 4], [0, 4, 5]])
        self.assertTrue(np.array_equal(shortest_path2,expected_path2))

if __name__ == '__main__':
    unittest.main()
