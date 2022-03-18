from lifelines import CoxPHFitter
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("rossi.csv",encoding="shift-jis")

model=CoxPHFitter()
model.fit(df,duration_col="week",event_col="arrest")

model.print_summary()

pred=model.predict_survival_function(df)
plt.plot(pred[0].values)#1人目のデータ
plt.plot(pred[1].values)#2人目のデータ
plt.show()

model.plot()
plt.show()
