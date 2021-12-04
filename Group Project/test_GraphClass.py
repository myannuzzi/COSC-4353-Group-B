import unittest
from GraphClass import Graph
import numpy as np
import os

class TestGraph(unittest.TestCase):

    def test_setName(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.setName("Graph1")
        self.assertEqual(test.name, "Graph1")

    def test_getName(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        name = test.getName()
        self.assertEqual(name, "TestGraph1")
    
    def test_insertNode(self):
        # Check both number of nodes and the matrices are equal
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

        newMatrix = np.array([[0,1,1,0,0,0],
							[1,0,1,1,1,0],
							[1,1,0,1,0,0],
							[0,1,1,0,1,0],
							[0,1,0,1,0,0]
                            [0,0,0,0,0,0]])

        test = Graph("TestGraph", adjMatrix, False, False)
        self.assertEquals(int(test.nodeCount), 6)
        self.assertTrue(np.array_equal(test.adjMatrix,newMatrix))

    def test_insertEdge(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.insertEdge(1,1)
        self.assertEqual(test.adjMatrix(0,0), 1)

    def test_removeNode(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

        newMatrix = np.array([[0,1,1,1],
							[1,0,1,0],
							[1,1,0,1],
							[1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.removeNode(1)
        self.assertTrue(np.array_equal(test.adjMatrix,newMatrix))

    def test_removeEdge(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

        newMatrix = np.array([[0,1,0,0,0],
							[1,0,1,1,1],
							[0,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

        test = Graph("TestGraph", adjMatrix, False, False)
        test.removeEdge(3,1)
        self.assertTrue(np.array_equal(test.adjMatrix,newMatrix))

    def test_setEdgeWeight(self):
        # Create object with weighted graph
        # Test with both weight and unweighted

        # Unweighted
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        unweighted = test.setEdgeWeight(1,1,4)
        self.assertEqual(unweighted, -1)

        # Weighted
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, True, False)
        unweighted = test.setEdgeWeight(1,1,4)
        newMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        #self.assertTrue()
        pass

    def test_getEdgeWeight(self):
        # Test for both weighted and unweighted
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
        nodeCount = test.getNodeCount
        self.assertEqual(nodeCount, 5)

    def test_getEdgeCount(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        edgeCount = test.getEdgeCount()
        self.assertEqual(edgeCount,7)

    def test_getMatrix(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        newMatrix = test.getMatrix()
        self.assertTrue(np.array_equal(test.adjMatrix,newMatrix))
        

    def test_save(self):
        PATH = './adjMatrix.csv'
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.save()
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            flag = True
        else: 
            flag = False

        # Should check the file exists and return true, which is then checked by the test
        self.assertTrue(flag)
	
if __name__ == '__main__':
	unittest.main()
