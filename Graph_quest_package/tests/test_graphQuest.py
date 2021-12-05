# Unit test file for graphQuest package
import unittest
from testQuest import Graph
import numpy as np
import os


class TestGraphQuestPackage(unittest.TestProgram):
    def test_constructor(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getName(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_setName(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_isWeighted(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_isDirected(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getNodeCount(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getEdgeCount(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getAdjMatrix(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getAdjList(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getNodeList(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getEdgeList(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_createAdjList(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_createNodeList(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_insertNode(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_removeNode(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_insertEdge(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_removeEdge(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getEdgeWeight(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass
    
    def test_setEdgeWeight(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_getEdgeDirection(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    def test_setEdgeDirection(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)

        pass

    # Add other test functions below


# init main section
if __name__ == '__main__':
    unittest.main()
