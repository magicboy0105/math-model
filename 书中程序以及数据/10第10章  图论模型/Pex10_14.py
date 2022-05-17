#程序文件Pex10_14.py
import numpy as np
import networkx as nx
import pandas as pd
import pylab as plt
a=pd.read_excel("Pdata10_14.xlsx",header=None)
b=a.values; b[np.isnan(b)]=0
c=np.zeros((8,8))  #邻接矩阵初始化
c[0:7,1:8]=b  #构造图的邻接矩阵
G=nx.Graph(c)
T=nx.minimum_spanning_tree(G)  #返回可迭代对象
d=nx.to_numpy_matrix(T)  #返回最小生成树的邻接矩阵
print("邻接矩阵c=\n",d)
W=d.sum()/2+5  #求油管长度
print("油管长度W=",W)
s=dict(zip(range(8),range(1,9))) #构造用于顶点标注的标号字典
plt.rc('font',size=16); pos=nx.shell_layout(G)
nx.draw(T,pos,node_size=280,labels=s,node_color='r')
w=nx.get_edge_attributes(T,'weight')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.savefig('figure10_14.png'); plt.show()
