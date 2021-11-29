import numpy as np


# A utility function to find the
# vertex with minimum dist value, from
# the set of vertices still in node_list
def min_distance(dist,node_list):
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
    while(parent[j] != -1):
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

  #Parent array to store shortest path tree
  parent = [-1] * n_row

  # Distance of source vertex from itself is always 0
  dist[src] = 0

  # Add all vertices in node_list
  node_list = []
  for i in range(n_row):
    node_list.append(i)

  #Find shortest path for all vertices
  while node_list:

    # Pick the minimum dist vertex
    # from the set of vertices
    # still in node_list
    min_vertex = min_distance(dist,node_list)

    # remove min element	
    #node_list.remove(min_vertex)

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
    path_list.append(get_path(parent,i))
  return path_list

node_list = dijkstra('graph1weightedMat.csv', 0)
#print(node_list)


def print_min_path(node_list):
  for path in node_list:
    len_path = len(path)
    print("Min path from " + str(path[0]) + " to " + str(path[len_path-1]), end=" ---> ")
    for node in path:
      print(node, end=" ")
    print("\n")

print_min_path(node_list)
