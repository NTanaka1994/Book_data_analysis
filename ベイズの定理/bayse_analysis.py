import pandas as pd

df=pd.read_csv("golf.csv",encoding="shift-jis")

#天気と風でゴルフの因果関係を分析
columns=["天気","風"]
for col in columns:
    arr=df[col].values
    arr=list(set(list(arr)))
    for row in arr:
        deno=df.query("%s=='%s'"%(col,row))
        nume_y=deno.query("ゴルフ=='する'")
        nume_n=deno.query("ゴルフ=='しない'")
        print("p(Yes | %s)=%f"%(row,len(nume_y.values)/len(deno.values)))
        print("p(No | %s)=%f"%(row,len(nume_n.values)/len(deno.values)))
