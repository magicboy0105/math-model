#程序文件Pex11_13.py
import numpy as np
from sklearn.cluster import KMeans
a=np.array([[1, 3],[1.5, 3.2],[1.3, 2.8],[3, 1]])
md=KMeans(n_clusters=2)  #构建模型
md.fit(a)   #求解模型
labels=1+md.labels_   #提取聚类标签
centers=md.cluster_centers_   #提取聚类中心,每一行是一个聚类中心
print(labels,'\n-----------\n',centers)


