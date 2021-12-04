# UserTxt.py
# Python file for reading in user input and turning it into a graph
# Written by Mike Yannuzzi

# Create a list to hold user input
list = []

# Get number of nodes from user
print("Please input the number of nodes: ")
nodes = input(" Nodes")

print("Please enter the number of edges: ")
edges = input(" Edges")
list.append(nodes)
list.append(edges)

# Printout nodes and edges number
print(nodes)
print(edges) 

#Create an adjacency list and adjacency matrix with values
adjacencyMatrix = {nodes, nodes}
