# -*- coding: utf-8 -*-
"""LVADSUSR148_DeepakSridharanM_Lab4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jX2jFx9p2oxdUirUlreWFH5YDwTil-rM
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

df = pd.read_csv("/content/anomaly_train.csv")

df.head()

df.info()

df.isnull().sum()

df.duplicated().sum()

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
df["Location"]=l.fit_transform(df["Location"])

df.head()

# Select the features to be used for anomaly detection
features = ["Amount","Location"]

# Create a new dataframe with the selected features
X = df[features]

# Fit an Isolation Forest model to the data
model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(X)

# Predict the anomalies in the data
y_pred = model.predict(X)

print(y_pred)

# Add the predicted anomaly scores to the original dataframe
df["anomaly_score"] = model.decision_function(X)
anomalies = df.loc[df["anomaly_score"] < 0]

# predict
df_test= pd.read_csv("/content/anomaly_train.csv")
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
df_test["Location"]=l.fit_transform(df_test["Location"])
x=df_test[["Amount","Location"]]
df_values=x.values

find=df_values
result=[]
for i in find:
  z=model.predict([i])
  if z==[1]:
    result.append('no')
  elif z==[-1]:
    result.append('yes')

df_test['Anomaly']=result

plt.scatter(df["Amount"], df["anomaly_score"], label="Normal")
plt.scatter(anomalies["Amount"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Amount")
plt.ylabel("anomaly_score")
plt.legend()
plt.show()
print("")
df_test.head()