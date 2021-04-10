import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
#%matplotlib inline

df = pd.read_csv('GeneralEsportData1.csv', encoding='cp1252')

sums = df.groupby(df["Game"])["OnlineEarnings"].sum()

cmap = plt.cm.tab10
colors = cmap(np.arange(len(sums)) % cmap.N)

x = np.arange(len(sums.index))  # the label locations
width = 0.35  # the width of the bars
fig = plt.figure(figsize=(16, 16))
ax = fig.add_subplot()
rects1 = ax.bar(x, sums, width, color=colors)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Earnings')
ax.set_title('Absolute earnings per game')
ax.set_xticks(x)
ax.set_xticklabels(sums.index)
ax.legend(rects1, sums.index)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
fig.tight_layout()

plt.show()
