import pandas as pd, numpy as np, sklearn 
from sklearn.cluster import KMeans

load=pd.read_csv("./Documents/yellow2.csv")

"""
Q1
"""
pu=load.iloc[:, 5:7]    #上車經緯度 (column:5-6) 
do=load.iloc[:, 9:11]   #下車經緯度 (column:9-10)

#利用kmeans分成5群
kmeans_pu=KMeans(n_clusters=5)  
kmeans_do=KMeans(n_clusters=5)
kmeans_pu.fit(pu)
kmeans_do.fit(do)
#每個點皆會有一個label值 (0-4)
label_pu=kmeans_pu.labels_
label_do=kmeans_do.labels_

#計算每個pu cluster中的點個數
cnt_pu=np.zeros((5,1)) #cnt_pu=[[],[],[],[],[]]
for i in range(len(load)):
    if labels_pu[i]==0:
        cnt_pu[0]+=1
    elif label_pu[i]==1:
        cnt_pu[1]+=1
    elif label_pu[i]==2:
        cnt_pu[2]+=1
    elif label_pu[i]==3:
        cnt_pu[3]+=1
    else: 
        cnt_pu[4]+=1
        
#計算每個do cluster中的點個數
cnt_do=np.zeros((5,1)) #cnt_do=[[],[],[],[],[]]
for i in range(len(load)):
    if labels_do[i]==0:
        cnt_do[0]+=1
    elif label_do[i]==1:
        cnt_do[1]+=1
    elif label_do[i]==2:
        cnt_do[2]+=1
    elif label_do[i]==3:
        cnt_do[3]+=1
    else: 
        cnt_do[4]+=1        

#印出每個上車經緯度的中心點 且可以知道哪個最多       
print(kmeans_pu.cluster_centers_)
print(kmeans_pu.cluster_centers_)    

"""
Q2
"""
pu_time=load["tpep_pickup_datetime"]
do_time=load["tpep_dropoff_datetime"]

#type:pandas.core.series.Series

print(pu_time.value_counts()) #由多到少排好
print(do_time.value_counts())

"""
Q3
"""
plo=load["pickup_longitude"]
dlo=load["dropoff_longitude"]
pla=load["pickup_latitude"]
dla=load["dropoff_latitude"]
a_means=(plo[:]-dlo[:]).mean()
b_means=(pla[:]-dla[:]).mean()

for i in range(len(load)):
    if (plo[i]-dlo[i])>a_means or (pla[i]-dla[i])>b_means:
        trip[i]=1  #long trip
    else:
        trip[i]=0  #short trip

#count 屬於long trip的數目
print(np.count_nonzero(trip))




   
        
