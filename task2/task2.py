import pandas as pd
import numpy as np

dataset = "tmdb_5000_movies.csv"
df = pd.read_csv(dataset)

df_noid = df.iloc[:,1:] 
df_noid
df_noid.describe()
print(df_noid.describe(exclude="object"))

print(df_noid.mean())
print(df_noid.mean())
print(df_noid.sum())
print(df_noid.median())
print(df_noid.var())
print(df_noid.std())
print(df_noid.quantile(0.75))
