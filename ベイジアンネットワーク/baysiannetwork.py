from pgmpy.models import BayesianModel
from pgmpy.estimators import BicScore
from pgmpy.estimators import ConstraintBasedEstimator
from pgmpy.inference import VariableElimination
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import networkx as nx

df=pd.read_csv("boston.csv")
#df=pd.read_csv("iris.csv")

df_cate=df
columns=list(df.columns)
for col in columns:
    df_cate[col]=pd.cut(df[col],6)
df_cate

est=ConstraintBasedEstimator(df_cate)

skel,separating_sets=est.estimate_skeleton(significance_level=0.01)
pdag=est.skeleton_to_pdag(skel,separating_sets)
model=est.pdag_to_dag(pdag)
DAG_model=BayesianModel(model.edges())

nx.draw_circular(DAG_model, with_labels=True, arrowsize=30, node_size=800,alpha=0.3, font_weight='bold')
plt.savefig("beysiannetwork2.png")
plt.show()

DAG_model.fit(df_cate)
cpds=DAG_model.get_cpds()
txt=""
for cpd in cpds:
    txt=txt+str(cpd)+"\n"
txt=txt.replace(",","_to_")
txt=txt.replace("\n|","\n")
txt=txt.replace("|",",")
txt=txt.replace("-","")
txt=txt.replace("+","")
txt=txt.replace(" ","")
txt=txt.replace(",\n","")
f=open("baysenet2.csv","w",encoding="shift-jis")
f.write(txt)
f.close()
f=open("baysenet.txt","w",encoding="shift-jis")
f.write(txt)
f.close()
