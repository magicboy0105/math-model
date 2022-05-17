#程序文件Pex11_7.py
import numpy as np
from sklearn.decomposition import PCA
a=np.loadtxt("Pdata11_7.txt")
b=np.r_[a[:,1:4],a[:,-3:]]  #构造数据矩阵
md=PCA().fit(b)  #构造并训练模型
print("特征值为：",md.explained_variance_)
print("各主成分的贡献率：",md.explained_variance_ratio_)
print("奇异值为：",md.singular_values_)
print("各主成分的系数：\n",md.components_)  #每行是一个主成分
"""下面直接计算特征值和特征向量，和库函数进行对比"""
cf=np.cov(b.T)  #计算协方差阵
c,d=np.linalg.eig(cf) #求特征值和特征向量
print("特征值为：",c)
print("特征向量为：\n",d)
print("各主成分的贡献率为：",c/np.sum(c))
