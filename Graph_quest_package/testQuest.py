# Test graphQuest file because indents are weird
import numpy as np
# import file_to_mat
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import sys
from collections import defaultdict

# ------------------Graph Class-----------------------
class Graph:
    # Constructor
    def __init__(self, name, adjMatrix, isWeighted, isDirected):
        self.name = name
        # Sets the numpy matrix
        self.adjMatrix = adjMatrix
        #grabs node and edge count
        self.nodeCount = self.getNodeCount()
        self.egdeCount = self.getEdgeCount()
        # User defined graph type
        self.isWeighted = type(isWeighted)
        self.isDirected = type(isDirected)
        # Create the node list
        self.nodeList = self.createNodeList(self, self.nodeCount)
        self.adjList = self.createAdjList(self, adjMatrix)
    
    # createNodeList
    # Creates the node list for the graph constructor
    def createNodeList(self, nodeCount):
        nodeList = np.arange(1,self.nodeCount)
        return nodeList

    # setName
    # Sets name of graph
    def setName(self, name):
        self.name = name

    # getName
    # Gets name of graph
    def getName(self):
        return self.name
    
    # Insert node
    # Inserts node into graph (need to figure out about edge connections)
    def insertNode(self):
        copyMatrix = self.adjMatrix
        # New idea, create an array of 0's one row and column bigger than the original and copy the values over
        newMatrix = np.zeros(
            (int(self.nodeCount+1), int(self.nodeCount+1)), dtype=int)
        # loop through and add in values from previous matrix to new one
        for i in range(self.nodeCount):
            for j in range(self.nodeCount):
                newMatrix[i][j] = copyMatrix[i][j]
        # Set new matrix values
        self.adjMatrix = newMatrix

    # Remove node
    # Removes node from graph (needs to remove related edges from node that was removed)
    def removeNode(self, value):
        # Remove both row and column from adjacency matrix
        if(value < 0 or value > self.nodeCount):
            print("Node out of bounds")
            return -1
        # Create new matrix
        newMatrix = self.adjMatrix
        # Delete row first
        newMatrix = np.delete(newMatrix, value, 0)
        # print(newMatrix)
        # Next delete column
        newMatrix = np.delete(newMatrix, value, 1)
        # print(newMatrix)
        print("Deleted node " + str(value))
        self.adjMatrix = newMatrix

    # Insert edge
    # Inserts edge into graph (needs a source node and destination node, undirected or directed, can be self referencing)
    def insertEdge(self, a, b):
        # Check if the edge values are out of place first
        if((a > self.nodeCount or a < 1) or (b > self.nodeCount or b < 1)):
            print("Node index out of bounds")
            return -1

        newMatrix = self.adjMatrix
        newMatrix[int(a-1), int(b-1)] = 1
        newMatrix[int(b-1), int(a-1)] = 1
        print("Edge added between nodes " + str(a) + " and " + str(b))
        self.adjMatrix = newMatrix

    # Remove edge
    # Removes edge from between two nodes (needs node a, node b, and edge. Need to work on how multiple edges work)
    def removeEdge(self, a, b):
        # Sets edge value in matrix to 0
        # Check if the edge values are out of place first
        if (a > self.nodeCount or a < 1) or (b > self.nodeCount or b < 1):
            print("Node index out of bounds")
            return -1

        newMatrix = self.adjMatrix
        newMatrix[int(a-1), int(b-1)] = 0
        newMatrix[int(b-1), int(a-1)] = 0
        print("Edge removed between nodes " + str(a) + " and " + str(b))
        self.adjMatrix = newMatrix

    # Set edge weight
    # Sets the value and direction of an edge between two nodes (or one node if self referencing)
    def setEdgeWeight(self, a, b, weight):
        # CHECK IF WEIGHTED GRAPH
        if(self.isWeighted != True):
            print("Cannot be done on an unweighted graph...")
            return
        # Sets edge value in matrix to 0
        # Check if the edge values are out of place first
        if((a > self.nodeCount or a < 1) or (b > self.nodeCount or b < 1)):
            print("Node index out of bounds")
            return -1

        newMatrix = self.adjMatrix
        newMatrix[int(a-1), int(b-1)] = weight
        newMatrix[int(b-1), int(a-1)] = weight
        print("Edge weight between nodes " + str(a) +
              " and " + str(b) + "changed to: " + str(weight))
        self.adjMatrix = newMatrix

    # Get edge weight
    # Get's edge weight between two nodes
    def getEdgeWeight(self, a, b):
        # CHECK IF WEIGHTED GRAPH
        if(self.isWeighted != True):
            print("Cannot be done on an unweighted graph...")
            return
        # Sets edge value in matrix to 0
        # Check if the edge values are out of place first
        if((a > self.nodeCount or a < 1) or (b > self.nodeCount or b < 1)):
            print("Node index out of bounds")
            return -1
        weight = self.adjMatrix[int(a), int(b)]
        return weight

    # NodeCount
    # Gets count of number of nodes in graph
    def getNodeCount(self):
        # Call dim on passed in matrix to get node count
        nodeCount = self.adjMatrix.shape
        return nodeCount[0]

    # EdgeCount
    # Gets count of number of nodes in graph
    def getEdgeCount(self):
        # Use numpy to grab the unique count of 1's and 0's
        unique, count = np.unique(self.adjMatrix, return_counts=True)
        d = dict(zip(unique, count))
        edgeCount = int((d.get(1))/2)
        return edgeCount
    
    # getMatrix
    # Returns matrix for graph
    def getMatrix(self, print):
        newMatrix = self.adjMatrix
        if print == True:
            print(self.adjMatrix)
        return newMatrix

    # getEdgeDirection
    # Gets the direction of an edge in a directed graph
    def getEdgeDirection(self, a, b):
        if self.isDirected == False:
            print("Cannot use this function on an undirected graph")
            return
        else:
            print("Add more here")
    
    # setEdgeDirection
    # Sets the edge direction between two nodes in a directed graph
    def setEdgeDirection(self, a, b):
        pass
    
    def getNodeList(self):
        return self.nodeList

    # createAdjList
    # Creates adjacency list from adjcency matrix
    def createAdjList(self):
        adjList = defaultdict(list)
        for i in range(self.getNodeCount):
            for j in range 
        pass

    # getAdjList
    # Returns adjList for graph
    def getAdjList(self, print):
        if print == True:
            print(self.adjList)
        return self.adjList


# Algorithm function sections
# # ------------------BFS-----------------------
# # input_folder = 'Adjacency matrices'

# # inputs_list = []

# # for f1, f2, f3 in os.walk(input_folder):
# #     for file in f3:
# #         inputs_list.append(os.path.join(f1, file))

# # print(inputs_list)
# # # given_file = int(input("choose one file from the available inputs as a number starting with 1: "))
# # given_file = 1

# # # given_num = int(input("enter a number between 0 to 4 to search in the graph: "))
# # given_num = 1 

# # #  for the purpose of testing, instead of taking user input I am passing an integer


# # g = file_to_mat.file_to_matrix(input_folder, given_file)
# # # print(g)


# def matrix_to_list(matrix_input):
#     graph = {}
#     for i, node in enumerate(matrix_input):
#         adj = []
#         for j, connected in enumerate(node):
#             if connected:
#                 adj.append(j)
#         graph[i] = adj
#     return graph


# # matrix = [[0, 19, 5, 0, 0],
# #           [19, 0, 5, 9, 2],
# #           [5, 5, 0, 1, 6],
# #           [0, 9, 1, 0, 1],
# #           [0, 2, 6, 1, 0]]


# def bfs(graph, v):
#     visited = []
#     Q = [v]
#     while Q:
#         v = Q.pop(0)
#         visited.append(v)
#         for n in graph[v]:
#             if n not in Q and \
#                     n not in visited:
#                 Q.append(n)
#     return visited


# gr = matrix_to_list(g)
# # print(gr)
# print("The breadth first search result on the given number is: ")
# print(bfs(gr, given_num))

#-------------------------PD-------------------------------------




#-------------------------Minimum Spanning Tree------------------



#-------------------------Cycle Detection------------------------


#-------------------------Dijsktra's-----------------------------




#-------------------------NetworkX Visualize---------------------
# create's NetworkX object that works with Graph object
def graphX(graph):
    pass