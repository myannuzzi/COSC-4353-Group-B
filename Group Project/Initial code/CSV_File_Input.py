import pandas as pd

# Importing the dataframes in CSV format
df_1 = pd.read_csv("C:/Users/user/Downloads/IP_addresses.csv", delimiter='None')
df_2 = pd.read_csv("C:/Users/user/Downloads/Book1.csv",delimiter='None')

# Converting the xlsx data file into CSV file format and importing the dataframe
file = pd.read_excel("C:/Users/user/Downloads/Ages_and_occupations.xlsx")
file.to_csv ("test.csv", index = None, header=True)
df_3 = pd.DataFrame(pd.read_csv("test.csv"))

# Printing the dataframes
print(df_1)
print(df_2)
print(df_3)
