import numpy as np
import pandas as pd
from pyDOE2 import fracfact

var={-1:"static",1:"dynamic"}
pointa={-1:"Yes",1:"No"}
code={-1:"few",1:"many"}
func={-1:"few",1:"many"}

doe=fracfact("a b c ab")

out=[]
tmp=[]
for i in range(len(doe)):
    out.append([var[doe[i][0]],pointa[doe[i][1]],code[doe[i][2]],func[doe[i][3]]])

df=pd.DataFrame(out)
df.columns=["var","pointa","code","func"]
index=[]
for i in range(1,len(out)+1,1):
    index.append("第%d実験"%(i))
df.index=index
df.to_csv("DoE_Frame.csv",index=False,encoding="shift-jis")
