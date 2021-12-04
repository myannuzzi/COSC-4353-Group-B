
# UNIT TESTING


df = pd.DataFrame([["A", "B"], ["C", "A"], ["B", "D"], ["Z", "B"], ["A", "C"] , ["A", "D"],  ["A", "D"]],
                      columns=["Column1", "Column2"])

# Dataframe
print("Actual Dataframe")
print(df)
print("\n")

# Converting dataframe to Adjacency Matrix
df_adj = df_to_adj_matrix(df.Column1, df.Column2)
print("Adjacency Matrix Dataframe")
print(df_adj)
print("-----------Testing passed--------------")
print("\n")

# Converting Adjacency Matrix Dataframe to Original Dataframe
print("Original Dataframe")
print(adj_mat_to_df(df_adj, ["Column1", "Column2"]))
print("-----------Testing passed--------------")
print("\n")


# Testing for graph1list.txt edge list
edge_list1= get_edgelist_from_graph("graph1list.txt")
print("Edge List for graph1list.txt : ")
print(edge_list1)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph1list.txt adjacency matrix
adj_mat1 = get_adj_mat("graph1list.txt")
print("Adjacency Matrix for graph1list.txt: ")
print(adj_mat1)
print("-----------Testing passed--------------")
print("\n")


# Testing for graph2list.txt edge list
edge_list2= get_edgelist_from_graph("graph2list.txt")
print("Edge List for graph2list.txt : ")
print(edge_list2)
print("-----------Testing passed--------------")
print("\n")


# Testing for graph2list.txt adjacency matrix
adj_mat2 = get_adj_mat("graph2list.txt")
print("Adjacency Matrix for graph2list.txt: ")
print(adj_mat2)
print("-----------Testing passed--------------")
print("\n")


# Testing for graph3list.txt edge list
edge_list3= get_edgelist_from_graph("graph3list.txt")
print("Edge List for graph3list.txt : ")
print(edge_list3)
print("-----------Testing passed--------------")
print("\n")


# Testing for graph3list.txt adjacency matrix
adj_mat3 = get_adj_mat("graph3list.txt")
print("Adjacency Matrix for graph3list.txt: ")
print(adj_mat3)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph4list.txt edge list
edge_list4= get_edgelist_from_graph("graph4list.txt")
print("Edge List for graph4list.txt : ")
print(edge_list4)
print("-----------Testing passed--------------")
print("\n")


# Testing for graph4list.txt adjacency matrix
adj_mat4 = get_adj_mat("graph4list.txt")
print("Adjacency Matrix for graph4list.txt: ")
print(adj_mat4)
print("-----------Testing passed--------------")
print("\n")


# Testing for graph1mat.csv adjacency matrix
adj_mat_unweighted1 =csv_to_numpy_adjmat('graph1mat.csv')
print("Adj Matrix of Unweighted CSV file graph1mat.csv")
print(adj_mat_unweighted1)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph2mat.csv adjacency matrix
adj_mat_unweighted2 =csv_to_numpy_adjmat('graph2mat.csv')
print("Adj Matrix of Unweighted CSV file graph2mat.csv")
print(adj_mat_unweighted2)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph3mat.csv adjacency matrix
adj_mat_unweighted3 =csv_to_numpy_adjmat('graph3mat.csv')
print("Adj Matrix of Unweighted CSV file graph3mat.csv")
print(adj_mat_unweighted3)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph1weightedMat.csv adjacency matrix
adj_mat_weighted1 =csv_to_numpy_adjmat('graph1weightedMat.csv')
print("Adj Matrix of Weighted CSV file graph1weightedMat.csv")
print(adj_mat_weighted1)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph2weightedMat.csv adjacency matrix
adj_mat_weighted2 =csv_to_numpy_adjmat('graph2weightedMat.csv')
print("Adj Matrix of Weighted CSV file graph2weightedMat.csv")
print(adj_mat_weighted2)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph3weightedMat.csv adjacency matrix
adj_mat_weighted3 =csv_to_numpy_adjmat('graph3weightedMat.csv')
print("Adj Matrix of Weighted CSV file graph3weightedMat.csv")
print(adj_mat_weighted3)
print("-----------Testing passed--------------")
print("\n")

# Testing for graph4weightedMat.csv adjacency matrix
adj_mat_weighted4 =csv_to_numpy_adjmat('graph4weighted.csv')
print("Adj Matrix of Weighted CSV file graph4weighted.csv")
print(adj_mat_weighted4)
print("-----------Testing passed--------------")
print("\n")


# File is saved as csv and contains the adj matrix
adj_mat_to_csv(adj_mat_unweighted2)
adj_mat_to_csv(adj_mat_weighted2)
