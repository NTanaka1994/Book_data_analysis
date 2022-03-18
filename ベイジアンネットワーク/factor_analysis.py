from causalnex.structure.notears import from_pandas
from causalnex.structure import StructureModel
from causalnex.network import BayesianNetwork
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import networkx as nx

df=pd.read_csv("breast_cancer.csv")

SM=from_pandas(df)

pos=nx.spring_layout(SM,k=60)
nx.draw_network_labels(SM)
edge_width=[ d['weight']*0.3 for (u,v,d) in SM.edges(data=True)]
nx.draw_networkx_labels(SM, pos)
nx.draw_networkx(SM,pos,node_size=4000,arrowsize=20,alpha=1.0,edge_color='b',width=edge_width)
plt.show()
