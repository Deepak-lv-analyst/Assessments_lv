# -*- coding: utf-8 -*-
"""LVADSUSR148_DeepakSridharan_m_clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18q9R8_LHQONWf0FExwIbtaHPNUiriYby
"""

import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings("ignore")

df=pd.read_csv('/content/Mall_Customers.csv')

df.head()

df.shape

df.isna().sum()

df.dropna(inplace=True)

df.isna()

df.duplicated().sum()

plt.figure(figsize=(10,6))
sns.boxplot(data=df)

plt.figure(figsize=(10, 5))
sns.distplot(df['Annual Income (k$)'])
plt.title('Distribution of Annual Income (k$)')
plt.xlabel('Range of Annual Income (k$)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 5))
sns.distplot(df['Age'])
plt.title('Distribution of Age')
plt.xlabel('Range of Age)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=df,)
plt.title('Gender Distribution')
plt.show()

#  Histograms for numerical columns
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Age')

plt.subplot(1, 3, 2)
sns.histplot(df['Annual Income (k$)'], kde=True)
plt.title('Distribution of Annual Income')

plt.subplot(1, 3, 3)
sns.histplot(df['Spending Score (1-100)'], kde=True)
plt.title('Distribution of Spending Score')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(data=df,x="Annual Income (k$)",y="Spending Score (1-100)",hue="Gender")
plt.show()

plt.figure(figsize=(10,15))
sns.pairplot(data=df,hue="Gender")
plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.iloc[:, 2:])

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
df['Gender']=l.fit_transform(df['Gender'])

selected_features = scaled_features

from sklearn.cluster import KMeans

wcss_list = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(selected_features)
    wcss_list.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss_list, marker='o', linestyle='--',c="blue")
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.xticks(np.arange(1, 11, 1))
plt.show()

from sklearn.cluster import KMeans

num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
y_pred= kmeans.fit_predict(selected_features)
df['cluster'] =y_pred

kmeans.labels_

#Scatterplot of the clusters
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'Annual Income (k$)',y = 'Spending Score (1-100)',hue="cluster",
                 palette=['green','orange','brown','dodgerblue','red'], legend='full',data = df  ,s = 60 )
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Spending Score (1-100) vs Annual Income (k$)')
plt.show()

from sklearn.metrics import silhouette_score
silhouette_score(df, y_pred)

plt.figure(figsize=(10, 6))
colors = ['purple', 'red', 'blue', 'green', 'yellow']
for i in range(5):
    plt.scatter(df["Age"][df.cluster == i], df["Annual Income (k$)"][df.cluster == i], c=colors[i], label=f'Cluster {i+1}', s=60)
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
plt.title('Customer Segmentation')
plt.legend()
plt.show()

for i in range(5):
    cust = df[df["cluster"]==i]
    print(f'Number of customers in group {i} = {len(cust)}')
    print(f'They are - {cust["CustomerID"].values}')
    print("--------------------------------------------")