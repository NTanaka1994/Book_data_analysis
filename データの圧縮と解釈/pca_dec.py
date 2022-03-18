from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("wine.csv")
y_name="Wine"
y=df[y_name].values
x_tab=df.drop(y_name,axis=1)
x_name=x_tab.columns
x=x_tab.values

model=PCA()
model.fit(x)
con=model.explained_variance_ratio_
fac=model.components_
dff=pd.DataFrame(fac)
dfc=pd.DataFrame(con)
dff.columns=x_name
index=[]
for i in range(len(fac)):
    index.append("第%d主成分"%(i+1))
dff.index=index
dfc.columns=["寄与率"]
dfc.index=index
dfcc=dfc.cumsum()
dfcc.columns=["累積寄与率"]
dff=pd.concat([dff,dfc,dfcc],axis=1)

factor=[]
for i in range(len(fac)):
    factor.append(np.sqrt(con[i])*fac[i])
dffac=pd.DataFrame(factor)
dffac.columns=x_name
dffac.index=index

tx=model.transform(x)
plt.scatter(tx[:,0],tx[:,1],c=y,cmap="brg")
plt.show()
