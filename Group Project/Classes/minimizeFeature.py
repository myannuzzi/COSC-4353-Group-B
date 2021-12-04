import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os
import file_to_mat
import sys

INF = 999
try:
    # number of vertices in graph
    nodes = int(input("Enter number of nodes (The limit is 5 as of now to avoid major complexity): "))
    # creating graph by adjacency matrix method
    edges = int(input("Enter number of edges: "))
except:
    print("enter integers only")
    sys.exit(1)

# commit to feature branch

# nodes = int(input("Enter number of nodes: "))
# # creating graph by adjacency matrix method
# edges = int(input("Enter number of edges: "))

# g = np.array([[0, 19, 5, 0, 0],
#               [19, 0, 5, 9, 2],
#               [5, 5, 0, 1, 6],
#               [0, 9, 1, 0, 1],
#               [0, 2, 6, 1, 0]])

input_folder = 'Minimizing-inputs'

inputs_list = []

for f1, f2, f3 in os.walk(input_folder):
    for file in f3:
        inputs_list.append(os.path.join(f1, file))

print(inputs_list)
given_file = int(input("choose one file from the available inputs as a number starting with 0: "))

# file_name = ""
#
g = file_to_mat.file_to_matrix(input_folder, given_file)
#

# adj_list[] = {{1->2->5}, {2->1,3,5,6}
# {3->2,4,6}
# {4->3,6}
# {5->1,2,6}
# {6->2,3,4,5}}

# adj_list = {"{0 – > 1 – > 3}, {1 – > 2}, {2 – > 3}"}
#
# num_line = 6
#
# def convert(adj, num_lines):
#     # Initialize a matrix
#     matrix = [[0 for j in range(num_lines)]
#               for i in range(num_lines)]
#
#     for i in range(num_lines):
#         for j in adj[i]:
#             matrix[i][j] = 1
#
#     return matrix


# # cons.replace("'", "[")
# li = cons.split('\n')
# li2 = [e.split(',') for e in li]
# g = []
# for e in li2:
#     li4 = []
#     for j in e:
#         li4.append(int(j))
#     g.append(li4)
# print(li3)

# print(g)
#
# print(df)

selected_node = [0, 0, 0, 0, 0]

selected_node[0] = True
# print("before",selected_node)

# printing for edge and weight
# print("Edge : Weight\n")
out = []
edge_out = []
edge_out2 = []
weights = []

while edges < nodes - 1:

    minimum = INF
    a = 0
    b = 0
    for m in range(nodes):
        if selected_node[m]:
            for n in range(nodes):
                if (not selected_node[n]) and g[m][n]:
                    # not in selected and there is an edge
                    if minimum > g[m][n]:
                        minimum = g[m][n]
                        a = m
                        b = n
    out += [[str(a) + " - " + str(b)] + [str(g[a][b])]]
    edge_out += [str(a)]
    edge_out2 += [str(b)]
    weights += [str(g[a][b])]
    df2 = pd.DataFrame(out, columns=["Edge", "Weight"])
    # print(df2)
    # print("out", out)
    selected_node[b] = True
    edges += 1

# print(edge_out)
# print(edge_out2)
# print(weights)
try:
    print("The dataframe for minimum spanning tree graph is: ")
    print(df2)
    # print(df2.values.tolist())
    print(selected_node)
except:
    print("Enter appropriate values for nodes and edges and try again")
    sys.exit(1)

# graph for the dataframe

gr = nx.Graph()

for i in range(len(edge_out)):
    gr.add_edge(edge_out[i], edge_out2[i], weight=weights[i])
    # gr[edge_out[i]][edge_out2[i]]['weight'] = weights[i]

# for e in gr.edges():
#     gr[e[0]][e[1]] = weights[e]
#
# nx.set_edge_attributes(gr, values=weights, name='weight')

print("It is going to show a", nx.info(gr))


def graph(gr):
    pos = nx.spring_layout(gr, seed=7)

    nx.draw_networkx_nodes(gr, pos, node_size=700)

    nx.draw_networkx_edges(gr, pos, width=6)

    nx.draw_networkx_labels(gr, pos, font_size=20, font_family="sans-serif")

    labels = nx.get_edge_attributes(gr, 'weight')
    nx.draw_networkx_edge_labels(gr, pos, font_size=20, edge_labels=labels)

    return plt.show()


graph(gr)
