# import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("marketing_campaign.csv")
df.head()
X = df.iloc[:,1:22]  #independent columns
y = df.iloc[:,-1]

corrmat = df.corr()
top_corr_features = corrmat.index

plt.rcParams.update(plt.rcParamsDefault)

# plot heatmap of correlation matrix
plt.figure(figsize=(18,22))
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")
plt.show()