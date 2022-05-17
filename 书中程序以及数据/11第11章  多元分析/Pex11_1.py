#程序文件Pex11_1.py
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
x0=np.array([[1.24,1.27], [1.36,1.74], [1.38,1.64], [1.38,1.82], [1.38,1.90], [1.40,1.70],
    [1.48,1.82], [1.54,1.82], [1.56,2.08], [1.14,1.78], [1.18,1.96], [1.20,1.86],
    [1.26,2.00], [1.28,2.00], [1.30,1.96]])   #输入已知样本数据
x=np.array([[1.24,1.80], [1.28,1.84], [1.40,2.04]])  #输入待判样本点数据
g=np.hstack([np.ones(9),2*np.ones(6)])  #g为已知样本数据的类别标号
v=np.cov(x0.T)  #计算协方差
knn=KNeighborsClassifier(2,metric='mahalanobis',metric_params={'V': v}) #马氏距离分类
knn.fit(x0,g); pre=knn.predict(x); print("马氏距离分类结果：",pre)
print("马氏距离已知样本的误判率为：",1-knn.score(x0,g))
knn2=KNeighborsClassifier(2)  #欧氏距离分类
knn2.fit(x0,g); pre2=knn2.predict(x); print("欧氏距离分类结果：",pre2)
print("欧氏距离已知样本的误判率为：",1-knn2.score(x0,g))
