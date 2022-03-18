#時系列データの分解
from statsmodels import api as sm
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("chingin.csv",encoding="shift-jis")
TSR=sm.tsa.seasonal_decompose(df["賃金指数"].values, period=6)
#TSR=sm.tsa.seasonal_decompose(df["感染者数"].values, freq=7)
TSR.plot()
plt.show()
trend=TSR.trend
seasonal=TSR.seasonal
residual=TSR.resid
plt.plot(trend)
plt.show()
plt.plot(seasonal)
plt.show()
plt.plot(residual)
plt.show()
