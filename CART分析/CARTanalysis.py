from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import DecisionTreeRegressor as DTR
from sklearn.tree import export_graphviz as EG
from pydotplus import graph_from_dot_data as GFDD

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("breast_cancer.csv",encoding="shift-jis")
y_name="result"
y=df[y_name].values
x_table=df.drop(y_name,axis=1)
x_name=x_table.columns
x=x_table.values

#model=DTR()
model=DTC()
model.fit(x,y)
imp=model.feature_importances_
dfi=pd.DataFrame(imp)
dfi.index=x_name
dfi.columns=["result"]
dfi=dfi.sort_values("result",ascending=False)
print(dfi)
dfi.to_csv("feature_importance.csv")

class_name=list(set(y))
for i in range(len(class_name)):
    class_name[i]=str(class_name[i])
dotdata=EG(model,filled=True,rounded=True,class_names=class_name,feature_names=x_name,out_file=None)
graph=GFDD(dotdata)
graph.write_png("CART.png")

result=[]
for i in range(len(y)):
    for col in dfi.index:
        result.append([col,int(y[i]),df[col].values[i]])
dfr=pd.DataFrame(result)
dfr.columns=["name","y","x"]
cname=list(set(y))
for col in dfi.index:
    res=dfr.query("name==\""+col+"\"")
    plt.title(col)
    re=[]
    for name in cname:
        re.append(res.query("y=="+str(name))["x"].values)
    plt.boxplot(re,labels=cname,positions=cname)
    plt.scatter(res["y"].values,res["x"].values,cmap="brg_r",c=res["y"],marker="_")
    plt.savefig(col+".png")
    plt.clf()
