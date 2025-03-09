# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# data
flavors = ('Chocolate', 'Vanilla', 'Pistachio', 'Mango', 'Strawberry')
votes = (12, 11, 4, 8, 15)
# warna chart
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D', '#D53032')
#highlight data "strawberry"
explode = (0, 0, 0, 0, 0.1)

plt.title('Favorite Ice Cream Flavors') #judul pie chart
# visualisasi pie chart
plt.pie(
    votes,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    shadow=True
)
(plt.show())
