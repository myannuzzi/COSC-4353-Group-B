import file_to_mat
import os
import sys

input_folder = 'Adjacency matrices'

inputs_list = []

for f1, f2, f3 in os.walk(input_folder):
    for file in f3:
        inputs_list.append(os.path.join(f1, file))

print(inputs_list)
given_file = int(input("choose one file from the available inputs as a number starting with 1: "))

given_num = int(input("enter a number between 0 to 4 to search in the graph: "))


g = file_to_mat.file_to_matrix(input_folder, given_file)
# print(type(g))


def matrix_to_list(matrix_input):
    graph = {}
    for i, node in enumerate(matrix_input):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph


# matrix = [[0, 19, 5, 0, 0],
#           [19, 0, 5, 9, 2],
#           [5, 5, 0, 1, 6],
#           [0, 9, 1, 0, 1],
#           [0, 2, 6, 1, 0]]


def bfs(graph, v):
    visited = []
    Q = [v]
    while Q:
        v = Q.pop(0)
        visited.append(v)
        for n in graph[v]:
            if n not in Q and \
                    n not in visited:
                Q.append(n)
    return visited


gr = matrix_to_list(g)
print("The breadth first search result on the given number is: ")
print(bfs(gr, given_num))