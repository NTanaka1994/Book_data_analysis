import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("chingin.csv",encoding="shift-jis")
y=df["賃金指数"].values
Y=np.fft.fft(y)
Y=np.abs(Y)
plt.bar(range(len(Y))[0:int(len(Y)/2)],Y[0:int(len(Y)/2)])
plt.show()
