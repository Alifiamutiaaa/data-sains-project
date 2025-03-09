# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# memuat dataset
dataset = "tmdb_5000_movies.csv"
df = pd.read_csv(dataset)

# visualisasi histogram
plt.hist(df['budget'], bins=50)
plt.title('Movie Budget Distribution')
plt.xlabel('Budget')
plt.ylabel('Count')
plt.show()