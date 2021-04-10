import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv ('Twitch_user_data.csv')

data.info()
data.head()
data.describe()


for i in data.columns:
    if ' ' in i:
        data = data.rename(columns={i:i.replace(' ','_')})
for i in data.columns:
    if '(' in i:
        data = data.rename(columns={i:i.replace('(','_')})
for i in data.columns:
    if ')' in i:
        data = data.rename(columns={i:i.replace(')','_')})



data.head()

null_cols = [i for i in data.columns if data[i].isnull().any()]
null_cols
data['Partnered']=data.Partnered.map(lambda p:int(p))
data['Mature']=data.Mature.map(lambda p:int(p))
data.head()


data.Language.nunique()
plot = data.groupby('Language').Average_viewers.agg(['max','min','mean','count']).sort_values(by='max',ascending=False)
plot
plt.figure(figsize=(20,10))
sns.barplot(x=plot.index,y=plot['max'])
plt.title('Max Average views Vs Language')
plt.show()



plot2 = data.groupby('Language').Peak_viewers.agg(['max','min','mean','count']).sort_values(by='max',ascending=False)
plot2

plt.figure(figsize=(20,10))
sns.barplot(x=plot2.index,y=plot2['max'])
plt.title('Peak viewers Vs Language')
plt.show()

plt.figure(figsize=(14,6))
sns.scatterplot(y=data['Language'], x=data['Average_viewers'])


plt.title("earnings")
plt.xlabel("twitch earnings")
plt.ylabel("average")
plt.show()

data.groupby('Channel').Average_viewers.min().sort_values(ascending=False).head(10)

sns.scatterplot(x=data['Stream_time_minutes_'], y=data['Average_viewers'])
plt.show()