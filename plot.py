import pandas as pd
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('data for cutter plot.csv', delimiter=";")
df.head()
df2 = pd.read_csv('second_plot.csv', delimiter=';')
plt.figure()
fig, ax = plt.subplots(figsize=(9, 7), dpi=100)
ax.scatter('records', 'features', data=df)

for index, row in df.iterrows():
    if (int(df['records'][index]) > 15000) or (int(df['features'][index]) > 100):
        ax.annotate(df['id'][index], (df['records'][index] + 0.2, df['features'][index]), fontsize=8)

ax2 = mpl_il.inset_axes(plt.gca(), width='80%', height='70%', loc=1)
ax2.scatter(df2['records'], df2['features'], color='orange')
df2.apply(lambda x: ax2.annotate(x['id'], (x['records'] + 0.2, x['features']), fontsize=8), axis=1)
plt.show()
fig2 = ax.get_figure()
fig2.set_size_inches(8.5, 11, forward=False)
fig2.savefig('picure_3.png', dpi=300)
