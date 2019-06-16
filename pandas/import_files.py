import os
import pandas

#os.listdir("./files_to_import")

df1 = pandas.read_csv("./files_to_import/supermarkets.csv")
#print(df1)

df3 = pandas.read_excel("./files_to_import/supermarkets.xlsx")
#print(df3)

df4 = pandas.read_csv("./files_to_import/supermarkets-semi-colons.txt", sep=";")
#print(df4)

df2 = pandas.read_json("./files_to_import/supermarkets.json")
#print(df2)
#print(df2.loc[2:4,"Country":"Name"]) #indexing by labels
#print(df2.iloc[3:5,2:3])

#add a column
#print(df2.shape)

df2["Continent"] = df2.shape[0]*["North America"]
#print(df2)

df2["Continent"] = df2["Country"] + "," + "North America"
#print(df2)

#transpotion (pasar filas a columnas)
df2_t = df2.T
print(df2_t)

df2_t["My address"] =  ["Bla", "My City", "My Country", 10, 7, "My Name", "My State", "My Continent"]
print(df2_t)

df2 = df2_t.T
print(df2)