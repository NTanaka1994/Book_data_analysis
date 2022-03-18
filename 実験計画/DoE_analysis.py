import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("DoE_result.csv",encoding="shift-jis")

y_name="y"
y=df[y_name]
x=df.drop(y_name,axis=1)
data=[]
name=[]
ave=[]
pos=[]
apos=[]
tmp_data=[]
tmp_ave=[]
tmp_pos=[]
i=0
for col in x.columns:
    arr=x[col].values
    arr=list(set(arr))
    for row in arr:
        df_q=df.query("%s=='%s'"%(col,row))
        data.append(df_q[y_name].values)
        tmp_data.append(df_q[y_name].values)
        tmp_pos.append(i)
        mean=np.array(tmp_data)
        tmp_ave.append(np.mean(mean))
        pos.append(i)
        i=i+1
        name.append("%s_%s"%(col,row))
    tmp_data=np.array(tmp_data)
    ave.append(tmp_ave)
    apos.append(tmp_pos)
    tmp_data=[]
    tmp_ave=[]
    tmp_pos=[]

for i in range(len(ave)):
    plt.plot(apos[i],ave[i],marker="x")
plt.boxplot(data,labels=name,positions=pos)
plt.show()
