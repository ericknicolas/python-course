import pandas as pd

df1 = pd.DataFrame([[1,2,3],[4,5,6]])
print(df1)

df2 = pd.DataFrame([[1,2,3],[4,5,6]],columns=["Age","Value","Month"], index=["first","second"])
print(df2)

print(df2.Age)

print(df2.Age.max())