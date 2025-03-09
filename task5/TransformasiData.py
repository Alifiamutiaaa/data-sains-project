import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
import missingno as mno


dataset = "train123.csv"
df = pd.read_csv(dataset)
print(df.head(12))
print(df.info())
print(df.describe())

df.loc[df["LotFrontage"] == 0.0, "LotFrontage"] = np.nan
df.isnull().sum()[1:6]
print(mno.matrix(df, figsize = (20, 6)))
#print(df.head(12))
