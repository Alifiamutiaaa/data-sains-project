# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = "tmdb_5000_movies.csv"
df = pd.read_csv(dataset)
print(df.head(10))

# mengambil top 10 data berdasarkan popularity
top_10 = df.nlargest(10, 'popularity')

# visualisasi line graph
plt.plot(
    top_10['original_title'],
    top_10['popularity'],
)
plt.title('Top 10 Most Popular Movies')
plt.ylabel('popularity')
plt.xticks(rotation=90)
plt.xlabel('original_title')
plt.show()
