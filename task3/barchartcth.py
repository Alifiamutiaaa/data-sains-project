# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# memuat data
countries = ('Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Falkland Islands', 'French Guiana', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela')

populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085, 3481, 287750, 785409, 7107305, 32880332, 585169, 3470475, 28258770)

# convert menjadi dataframe
df = pd.DataFrame({
    'Country': countries,
    'Population': populations,
})

# mengurutkan berdasarkan 'Population'
df.sort_values(by='Population', inplace=True)

x_coords = np.arange(len(countries))
# mengatur warna chart
colors = ['#0000FF' for _ in range(len(df))]
colors[-2] = '#FF0000'

# visualisasi bar chart
plt.bar(x_coords, df['Population'], tick_label=df['Country'], color=colors)
plt.xticks(rotation=90)
plt.ylabel('Population (Millions)')
plt.title('South American Population')
plt.show()