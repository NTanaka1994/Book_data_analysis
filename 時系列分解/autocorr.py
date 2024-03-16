import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def autocorr(y):
    tmpC = []
    C = []
    for h in range(len(y)):
        for t in range(len(y)-h):
            tmpC.append((y[t]-np.mean(y))*(y[t+h]-np.mean(y)))
        C.append(sum(tmpC)/len(y))
        tmpC = []
    r = np.array(C) / C[0]
    return r

df = pd.read_csv("chingin.csv", encoding="shift-jis")
y = df["賃金指数"]
r = autocorr(y.values)
plt.bar(range(len(r))[0:24],r[0:24])
plt.show()
