import pandas as pd

# Return adjacency matrix pandas dataframe

def df_to_adj_matrix(df_col1, df_col2):
  cross_df = pd.crosstab(df_col1, df_col2)
  idx = cross_df.columns.union(cross_df.index)
  adj_df = cross_df.reindex(index=idx, columns = idx, fill_value = 0)
  return adj_df

# Returns pandas dataframe from adjacency matrix dataframe

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

## TESTING

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
print("\n")