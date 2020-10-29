import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\kajal\Desktop\eg.csv")
data.head()

X = data[["Tax", "Customer_No"]]
plt.scatter(X["Customer_No"],X["Tax"], c='black')
# plt.xlabel('No. of customer')
# plt.ylabel('Tax(in crores)')
# plt.show()

k=4
centroids = (X.sample(n=k))
plt.scatter(X["Customer_No"],X["Tax"], c='black')
plt.scatter(centroids["Customer_No"],centroids["Tax"], c='red')
# plt.xlabel('No. of customer')
# plt.ylabel('Tax(in crores)')
# plt.show()


diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Customer_No"]-row_d["Customer_No"])**2
            d2=(row_c["Tax"]-row_d["Tax"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(k):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    centroids_new = X.groupby(["Cluster"]).mean()[["Tax","Customer_No"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (centroids_new['Tax'] - centroids['Tax']).sum() + (centroids_new['Customer_No'] - centroids['Customer_No']).sum()
        print(diff.sum())
    centroids = X.groupby(["Cluster"]).mean()[["Tax","Customer_No"]]

    color=['blue','green','cyan','yellow']
for k1 in range(k):
    data=X[X["Cluster"]==k1+1]
    plt.scatter(data["Customer_No"],data["Tax"],c=color[k1])
plt.scatter(centroids["Customer_No"],centroids["Tax"],c='red')
plt.xlabel('No. of customers')
plt.ylabel('Tax (In crores)')
plt.show()
