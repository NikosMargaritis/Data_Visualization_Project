import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
#%matplotlib inline

df = pd.read_csv('GeneralEsportData1.csv', encoding='cp1252')

sums = df.groupby(df["Game"])["OnlineEarnings"].sum()

fig = plt.figure(figsize=(16, 16))
ax = fig.add_subplot()

def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%".format(pct)


wedges, texts, autotexts = ax.pie(sums, autopct=lambda pct: func(pct, sums),
                                  textprops=dict(color="w"))

ax.legend(wedges, sums.index,
          title="Games",
          loc="upper left",
          bbox_to_anchor=(1, 0, 0.5, 1))

ax.pie(sums)
ax.set_title("Total earnings percentages")
plt.show()