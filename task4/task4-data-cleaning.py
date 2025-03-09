# import library
import pandas as pd
import numpy as np

# load data
df = pd.read_csv("tahun-2021---data-event-non-budaya-di-kota-bandung.csv")
print(df.head())

# periksa tipe datanya utk masing2 varibael/kolom/fitur dengan .dtypes
print(df.dtypes)

df.dtypes.value_counts()


