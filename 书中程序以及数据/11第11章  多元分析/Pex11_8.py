#程序文件Pex11_8.py
import numpy as np
from scipy.stats import zscore
a=np.loadtxt("Pdata11_8.txt")
print("相关系数阵为：\n",np.corrcoef(a.T))
b=np.delete(a,0,axis=1) #删除第1列数据
c=zscore(b); r=np.corrcoef(c.T) #数据标准化并计算相关系数阵
d,e=np.linalg.eig(r) #求特征值和特征向量
rate=d/d.sum()  #计算各主成分的贡献率
print("特征值为：",d)
print("特征向量为：\n",e)
print("各主成分的贡献率为：",rate)
k=1; #提出主成分的个数
F=e[:,:k]; score_mat=c.dot(F) #计算主成分得分矩阵
score1=score_mat.dot(rate[0:k])  #计算各评价对象的得分
score2=-score1  #通过观测，调整得分的正负号
print("各评价对象的得分为：",score2) 
index=score1.argsort()+1   #排序后的每个元素在原数组中的位置
print("从高到低各个城市的编号排序为：",index)
