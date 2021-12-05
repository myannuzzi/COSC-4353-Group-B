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
        # Create edge list 

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
        if self.isDirected == False:
            print("Cannot perform this function on undirected graph")
            return
        else:
            print("Add more here")
    
    def getNodeList(self):
        return self.nodeList

    # createAdjList
    # Creates adjacency list from adjcency matrix
    def createAdjList(self):
        adjList = defaultdict(list)
        for i in range(self.getNodeCount):
            # for j in range 
            print("Adding to node: " + i)
            for j in range(self.getNodeCount):
                print("Adding to list of node: " + j)
                if self.adjMatrix[i][j] == 1 :
                    adjList.append(j)
        return adjList

    # getAdjList
    # Returns adjList for graph
    def getAdjList(self, print):
        if print == True:
            print(self.adjList)
        return self.adjList

    # isWeighted
    # Returns if graph is weighted
    def isWeighted(self):
        return self.isWeighted

    # isDirected
    # Returns if graph is directed
    def isDirected(self):
        return self.isDirected


#---------------------Pandas functions-----------------------


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
# Return adjacency matrix pandas dataframe
# For Unweighted graph
def df_to_adj_matrix(df_col1, df_col2):
    cross_df = pd.crosstab(df_col1, df_col2)
    idx = cross_df.columns.union(cross_df.index)
    adj_df = cross_df.reindex(index=idx, columns=idx, fill_value=0)
    return adj_df


# Returns pandas dataframe from adjacency matrix dataframe
# For Unweighted graph
def adj_mat_to_df(adj_df, column_list):
    headers = adj_df.columns
    edge_list = []
    for index, row in adj_df.iterrows():
        header_idx = 0
        for col in row:
            while col > 0:
                edge_list.append([index, headers[header_idx]])
                col -= 1
            header_idx += 1
    df = pd.DataFrame(edge_list, columns=column_list)
    return df


# Unweighted Graph

def get_edgelist_from_graph(fileName):
    f = open(fileName, "r")
    edge_list = []
    for line in f.readlines():
        node_list = line.strip().split('->')
        from_node = node_list[0]
        to_node_list = node_list[1].strip().split(',');
        for node in to_node_list:
            edge_list.append([int(from_node), int(node)])

    return np.array(edge_list)


# Unweighted graph

def get_adj_mat(fileName, zero_indexed=False):
    edge_list = get_edgelist_from_graph(fileName)
    if not zero_indexed:
        edge_list = [[x - 1 for x in edge] for edge in edge_list]

    size = len(set([n for e in edge_list for n in e]))
    adjacency = [[0] * size for _ in range(size)]
    for sink, source in edge_list:
        adjacency[sink][source] += 1

    return np.array(adjacency)


# # Weighted / Unweighted
# # Input :  CSV file consisting of adj matrix
# # Output : Numpy array of adj matrix

# def csv_to_numpy_adjmat(fileName):
#     adj_mat = np.genfromtxt(fileName, delimiter=',')
#     return np.array(adj_mat, dtype=np.int)


# Weighted / Unweighted
# Input : Numpy array of adj matrix
# Output :  CSV file consisting of adj matrix

def adj_mat_to_csv(Graph, path=""):
    np.savetxt(path + "adjMatrix.csv", Graph.getAdjMatrix(), delimiter=",", fmt='%i')
    print("The output will be stored outside the directory in a file called adjMatrix.csv")




#-------------------------Minimum Spanning Tree------------------



#-------------------------Cycle Detection------------------------



#-------------------------Dijsktra's-----------------------------
# A utility function to find the
# vertex with minimum dist value, from
# the set of vertices still in node_list
def min_distance(dist, node_list):
    minimum = float("Inf")
    min_index = -1
    for i in range(len(dist)):
        if dist[i] < minimum and i in node_list:
            minimum = dist[i]
            min_index = i
    return min_index


# Function to print shortest path from source to j using parent array
def get_path(parent, j):
    path = []
    while parent[j] != -1:
        path.append(j)
        j = parent[j]
    path.append(j)
    return [ele for ele in reversed(path)]


# This is the main function..
# it takes the input the files that you mentioned and give output as indicated
def dijkstra(fileName, src):
    adj_mat = np.genfromtxt(fileName, delimiter=',')
    adj_mat = np.array(adj_mat, dtype=np.int)
    n_row = len(adj_mat)
    n_col = len(adj_mat)

    # We need this to maintain the distance of each node from source
    dist = [float("Inf")] * n_row

    # Parent array to store shortest path tree
    parent = [-1] * n_row

    # Distance of source vertex from itself is always 0
    dist[src] = 0

    # Add all vertices in node_list
    node_list = []
    for i in range(n_row):
        node_list.append(i)

    # Find shortest path for all vertices
    while node_list:

        # Pick the minimum dist vertex
        # from the set of vertices
        # still in node_list
        min_vertex = min_distance(dist, node_list)

        # remove min element
        node_list.remove(min_vertex)

        # Update dist value and parent
        # index of the adjacent vertices of
        # the picked vertex. Consider only
        # those vertices which are still in
        # node_list
        for i in range(n_col):
            if adj_mat[min_vertex][i] and i in node_list:
                if dist[min_vertex] + adj_mat[min_vertex][i] < dist[i]:
                    dist[i] = dist[min_vertex] + adj_mat[min_vertex][i]
                    parent[i] = min_vertex
    path_list = []
    for i in range(1, len(dist)):
        path_list.append(get_path(parent, i))
    return path_list


def print_min_path(node_list):
    for path in node_list:
        len_path = len(path)
        print("Min path from " + str(path[0]) + " to " + str(path[len_path - 1]), end=" ---> ")
        for node in path:
            print(node, end=" ")
        print("\n")


#-------------------------NetworkX Visualize---------------------
# create's NetworkX object that works with Graph object
def graphX(graph):
    # First create networkx object
    gr = nx.Graph()
    pass