#程序文件Pex10_10.py
import numpy as np
import networkx as nx
List=[(1,2,20),(1,5,15),(2,3,20),(2,4,40),
      (2,5,25),(3,4,30),(3,5,10),(5,6,15)]
G=nx.Graph()
G.add_nodes_from(range(1,7))
G.add_weighted_edges_from(List)
c=dict(nx.shortest_path_length(G,weight='weight'))
d=np.zeros((6,6))
for i in range(1,7):
    for j in range(1,7): d[i-1,j-1]=c[i][j]
print(d)
q=np.array([80,90,30,20,60,10])
m=d@q  #计算运力，这里使用矩阵乘法
mm=m.min()  #求运力的最小值
ind=np.where(m==mm)[0]+1  #python下标从0开始，np.where返回值为元组
print("运力m=",m,'\n最小运力mm=',mm,"\n选矿厂的设置位置为：",ind)
