# Another test file

from testQuest import Graph
import numpy as np
print("Starting test for Graph class")

adjMatrix = np.array([[0,1,1,0,0],
					  [1,0,1,1,1],
					  [1,1,0,1,0],
					  [0,1,1,0,1],
					  [0,1,0,1,0]])

# Start!
# Test Constructor
# print("Pass...")
test = Graph("graph1", adjMatrix, False, False)
print(test)
# print("Node count is: " + str(test.nodeCount))
# print("Edge count is: " + str(test.edgeCount))

# Test weighted or directed
if test.isWeighted() == True:
    print("Graph is weighted")
else:
    print("Graph is not weighted")

if test.isDirected() == True:
    print("Graph is directed")
else:
    print("Grahp is not weighted")


# Test getName
testName = test.getName()
print("Name of Graph is = " + testName)

# Test setName
print("Testing setName")
test.setName("newName")
print("New name is: " + test.name)
print()

adjList = test.createAdjList()
print(adjList)




# # Test insertNode
# print("Testing insertNode")
# test.insertNode()
# print("Pass...")

# # Test insertEdge
# print("Testing insert edge")
# # print("Pass...")
# print("Adding edge between 1 and 4")
# test.insertEdge(1,4)
# print(test.adjMatrix)

# # Test removeNode
# print("Testing removeNode")
# test.removeNode(2)
# print("Pass...")
# print(test.adjMatrix)

# # Test removeEdge
# print("Testing removeEdge")
# test.removeEdge(1,4)
# print("Pass...")




# # Testing getNodeCount
# print("Testing getNodeCount")
# # print("Pass...")
# nodeCount = test.getNodeCount()
# print("Graph has " + str(nodeCount) + " nodes")

# # Testing getEdgeCount
# print("Testing getEdgeCount")
# edgeCount = test.getEdgeCount()
# print(edgeCount)
# # print("Pass...")

# # Testing save csv file
# # Need to fix file so it saves as integers
# print("Testing csv file save")
# test.save()

# # Testing get matrix
# print("Testing get matrix")
# matrix = test.getMatrix()
# print(matrix)

# # Testing algorithms
# # Detect cycle algorithm
