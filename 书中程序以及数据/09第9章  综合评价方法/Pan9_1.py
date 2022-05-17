#程序文件Pan9_1.py
from scipy.sparse.linalg import eigs
from numpy import array, hstack
a=array([[1,1/2,5,5,3],[2,1,7,7,5],[1/5,1/7,1,1/2,1/3],
        [1/5,1/7,2,1,1/2],[1/3,1/5,3,2,1]])
L,V=eigs(a,1);
CR=(L-5)/4/1.12  #计算矩阵A的一致性比率
W=V/sum(V); print("最大特征值为：",L)
print("最大特征值对应的特征向量W=\n",W)
print("CR=",CR)
B1=array([[1,1/3,1/2],[3,1,1/2],[2,2,1]])
L1,P1=eigs(B1,1); P1=P1/sum(P1)
print("P1=",P1)
B2=array([[1,3,2],[1/3,1,2],[1/2,1/2,1]])
t2,P2=eigs(B2,1); P2=P2/sum(P2)
print("P2=",P2)
B3=array([[1,4,3],[1/4,1,2],[1/3,1/2,1]])
t3, P3=eigs(B3,1); P3=P3/sum(P3)
print("P3=",P3)
B4=array([[1,3,2],[1/3,1,2],[1/2,1/2,1]])
t4, P4=eigs(B4,1); P4=P4/sum(P4)
print("P4=", P4)
B5=array([[1,2,3],[1/2,1,1/2],[1/3,2,1]])
t5, P5=eigs(B5,1); P5=P5/sum(P5)
print("P5=",P5)
K=hstack([P1,P2,P3,P4,P5])@W  #矩阵乘法
print("K=",K)
