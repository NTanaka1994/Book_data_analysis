from sklearn.ensemble import GradientBoostingClassifier as GBC
import pandas as pd

df = pd.read_csv("wine.csv")
y_name = "Wine"
y = df[y_name].values
x_tab = df.drop(y_name,axis=1)
x_name = x_tab.columns
x = x_tab.values

model = GBC()
model.fit(x, y)
imp = model.feature_importances_
dfi = pd.DataFrame(imp).T
dfi.columns = x_name
dfi.index=["imp"]
