#程序文件Pex10_15.py
import numpy as np
import networkx as nx
from networkx.algorithms.matching import max_weight_matching
a=np.array([[3,5,5,4,1],[2,2,0,2,2],[2,4,4,1,0],
            [0,2,2,1,0],[1,2,1,3,3]])
b=np.zeros((10,10)); b[0:5,5:]=a; G=nx.Graph(b)
s0=max_weight_matching(G)  #返回值为（人员，工作）的集合
s=[sorted(w) for w in s0]
L1=[x[0] for x in s]; L1=np.array(L1)+1  #人员编号
L2=[x[1] for x in s]; L2=np.array(L2)-4  #工作编号
c=a[L1-1,L2-1]  #提取对应的效益
d=c.sum()  #计算总的效益
print("工作分配对应关系为：\n人员编号：",L1)
print("工作编号：", L2); print("总的效益为：",d)

