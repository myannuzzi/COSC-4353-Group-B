import pandas as pd
import numpy as np


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


# Weighted / Unweighted
# Input :  CSV file consisting of adj matrix
# Output : Numpy array of adj matrix

def csv_to_numpy_adjmat(fileName):
    adj_mat = np.genfromtxt(fileName, delimiter=',')
    return np.array(adj_mat, dtype=np.int)


# Weighted / Unweighted
# Input : Numpy array of adj matrix
# Output :  CSV file consisting of adj matrix

def adj_mat_to_csv(adj_mat, path=""):
    np.savetxt(path + "adjMatrix.csv", adj_mat, delimiter=",", fmt='%i')


print("The output will be stored outside the directory in a file called adjMatrix.csv")
