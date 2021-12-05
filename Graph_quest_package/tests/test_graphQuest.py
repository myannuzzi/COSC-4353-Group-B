# Unit test file for graphQuest package
import unittest
import sys
import numpy as np
import os

# Importing from another directory
sys.path.insert(0,'D:/UH Fall 2021/4353 Software Design/Group project/repo/COSC-4353-Group-B/Graph_quest_package')
from testQuest import Graph

class TestGraphQuestPackage(unittest.TestCase):
    # Adding in setup and teardown to reduce code reusage
    def setUp(self):
        # print("setup")
        adjMatrix = np.array([[0, 1, 1, 0, 0],
                              [1, 0, 1, 1, 1],
                              [1, 1, 0, 1, 0],
                              [0, 1, 1, 0, 1],
                              [0, 1, 0, 1, 0]])
        self.test = Graph("TestGraph", adjMatrix, False, False)

    def tearDown(self):
        # print("teardown")
        pass

    def test_constructor(self):
        # print("test_constructor")
        pass

    def test_getName(self):
        print("test_getName")
        self.assertEqual(self.test.name,"TestGraph")

    def test_setName(self):
        print("test_setName")
        self.test.setName("DifferentName")
        self.assertEqual(self.test.name, "DifferentName")

    def test_isWeighted(self):
        print("test_isWeighted")
        self.assertFalse(self.test.isWeighted())

    def test_isDirected(self):
        print("test_isDirected")
        self.assertFalse(self.test.isDirected())
        pass

    def test_getNodeCount(self):
        print("test_getNodeCount")
        pass

    def test_getEdgeCount(self):
        print("test_getEdgeCount")
        pass

    def test_getAdjMatrix(self):
        print("test_getAdjMatrix")
        pass

    def test_getAdjList(self):
        print("test_getAdjList")
        pass

    def test_getNodeList(self):
        print("test_getNodeList")
        pass

    def test_getEdgeList(self):
        print("test_getEdgeList")
        pass

    def test_createAdjList(self):
        print("test_createAdjList")
        pass

    def test_createNodeList(self):
        print("test_createNodeList")
        pass

    def test_insertNode(self):
        print("test_insertNode")
        pass

    def test_removeNode(self):
        print("test_removeNode")
        pass

    def test_insertEdge(self):
        print("test_insertEdge")
        pass

    def test_removeEdge(self):
        print("test_removeEdge")
        pass

    def test_getEdgeWeight(self):
        print("test_getEdgeWeight")
        pass

    def test_setEdgeWeight(self):
        print("test_setEdgeWeight")
        pass

    def test_getEdgeDirection(self):
        print("test_getEdgeDirection")
        pass

    def test_setEdgeDirection(self):
        print("test_setEdgeDirection")
        pass

    # Add other test functions below


# init main section
if __name__ == '__main__':
    unittest.main()
