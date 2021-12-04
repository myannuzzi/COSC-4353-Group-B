# Put all code for features and classes here
# imports
import numpy as np

# Graph Class
class Graph:
	# Class that represents the node and edge graph. Also contains functions for adding and removing 	nodes and edges, naming and storing graphs.
	def __init__(self, name, adjMatrix, isWeighted, isDirected):
		self.name = name
		self.adjMatrix = adjMatrix
		self.nodeCount = self.getNodeCount()
		self.edgeCount = self.getEdgeCount()
		self.isWeighted = type(isWeighted)
		self.isDirected = type(isDirected)

	# Set name
	# Set's name of graph
	def setName(self,name):
		self.name = name

	# Get name
	# Get's name of graph
	def getName(self):
		return self.name

	# Insert node
	# Inserts node into graph (need to figure out about edge connections)
	def insertNode(self):
		copyMatrix = self.adjMatrix
		# New idea, create an array of 0's one row and column bigger than the original and copy the values over
		newMatrix = np.zeros((int(self.nodeCount+1), int(self.nodeCount+1)),dtype=int)
		# loop through and add in values from previous matrix to new one
		for i in range(self.nodeCount):
			for j in range(self.nodeCount):
				newMatrix[i][j] = copyMatrix[i][j]
		# Set new matrix values
		self.adjMatrix = newMatrix
		
	# Insert edge
	# Inserts edge into graph (needs a source node and destination node, undirected or directed, can be self referencing)
	def insertEdge(self, a, b):
		# Check if the edge values are out of place first
		if((a > self.nodeCount or a < 1) or (b > self.nodeCount or b < 1)):
			print("Node index out of bounds")
			return -1

		newMatrix = self.adjMatrix
		newMatrix[int(a-1),int(b-1)] = 1
		newMatrix[int(b-1),int(a-1)] = 1
		print("Edge added between nodes " + str(a) + " and " + str(b))
		self.adjMatrix = newMatrix
			
	# Remove node
	# Removes node from graph (needs to remove related edges from node that was removed)
	def removeNode(self,value):
		# Remove both row and column from adjacency matrix
		if(value < 0 or value > self.nodeCount):
			print("Node out of bounds")
			return -1
		# Create new matrix
		newMatrix = self.adjMatrix
		# Delete row first
		newMatrix = np.delete(newMatrix,value,0)
		# print(newMatrix)
		# Next delete column
		newMatrix = np.delete(newMatrix,value,1)
		# print(newMatrix)
		print("Deleted node " + str(value))
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
		newMatrix[int(a-1),int(b-1)] = 0
		newMatrix[int(b-1),int(a-1)] = 0
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
		newMatrix[int(a-1),int(b-1)] = weight
		newMatrix[int(b-1),int(a-1)] = weight
		print("Edge weight between nodes " + str(a) + " and " + str(b) + "changed to: " + str(weight))
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
		unique, count = np.unique(self.adjMatrix, return_counts = True)
		d = dict(zip(unique, count))
		edgeCount = int((d.get(1))/2)
		return edgeCount
	
	# getMatrix
	# Returns matrix for graph
	def getMatrix(self):
		newMatrix = self.adjMatrix
		return newMatrix

	# Output function
	# Create a csv file
	def save(self):
		# Put numpy array into csv file
		print("Saving file under 'adjmatrix.csv'")
		np.savetxt('adjMatrix.csv', self.adjMatrix, delimiter=",")


# Graph Algorithms
# Dijsktra's
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