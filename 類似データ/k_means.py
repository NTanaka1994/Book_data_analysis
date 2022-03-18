from sklearn import preprocessing
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

df=pd.read_csv("wine.csv")
x_tab=df.drop("category",axis=1)
x=x_tab.values
x_mm=preprocessing.minmax_scale(x)
model=KMeans(n_clusters=3)
model.fit(x_mm)
pred=model.predict(x_mm)
col=list(x_tab.columns)
col.append("category")
pred=pred.reshape(-1,1)
data=np.hstack((x,pred))
df_out=pd.DataFrame(data)
df_out.columns=col
df_out.to_csv("wine_cluster.csv",index=False)
