#程序文件Pex11_2.py
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
a=pd.read_excel("Pdata11_2.xlsx",header=None)
b=a.values
x0=b[:-2,1:-1].astype(float)  #提取已知样本点的观测值
y0=b[:-2,-1].astype(int)
x=b[-2:,1:-1]  #提取待判样本点的观察值
v=np.cov(x0.T)  #计算协方差
knn=KNeighborsClassifier(3,metric='mahalanobis',metric_params={'V': v}) #马氏距离分类
knn.fit(x0,y0); pre=knn.predict(x); print("分类结果：",pre)
print("已知样本的误判率为：",1-knn.score(x0,y0))

