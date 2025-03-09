# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# memuat data
temperature_c = [2, 1, 0, 0, 1, 5, 8, 9, 8, 5, 3, 2, 2]
hour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

# visualisasi line graph
plt.plot(
  hour,
  temperature_c
)
plt.show()
