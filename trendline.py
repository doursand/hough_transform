# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:05:23 2018

@author: doursand
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import argrelextrema
from scipy import stats
import numpy as np

df = pd.read_csv('c:\\users\\andre_000\desktop\ml pee\EURONEXT-CLA.csv')
df = pd.DataFrame(df, columns=['Last'])

#plt.plot(df)



n=4

# Find local peak
df['min'] = df.iloc[argrelextrema(df['Last'].values, np.less_equal, order=n)[0]]['Last']
df['max'] = df.iloc[argrelextrema(df['Last'].values, np.greater_equal, order=n)[0]]['Last']

y=df.iloc[:,-1].values

#redim X array as 1 dim vector
X=(df.index.values).astype(np.float64).reshape(-1,1)

#take care of NaN
finiteymask = np.isfinite(y)
yclean = y[finiteymask].reshape(-1,1)
Xclean = X[finiteymask]
plt.style.use('dark_background')
ax = plt.axes()
ax.set_axis_off()
plt.scatter(df.index, df['max'],c="white",s=1)
plt.savefig(fname="OUT.jpg", quality=100, bbox_inches='tight',transparent=True)
    
