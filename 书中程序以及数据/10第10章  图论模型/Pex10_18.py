#程序文件Pex10_18.py
import numpy as np,networkx as nx
import pylab as plt
from scipy.sparse.linalg import eigs
L=[(1,2),(2,3),(2,4),(3,4),(3,5),(3,6),
   (4,1),(5,6),(6,1)]
G=nx.DiGraph()
G.add_nodes_from(range(1,7))  #添加顶点集
G.add_edges_from(L)  #添加边集
B=np.array(nx.to_numpy_matrix(G))  #提取邻接矩阵
plt.rc('font',size=16); pos=nx.shell_layout(G)
nx.draw(G,pos,node_size=280,font_weight='bold',
        node_color='r',with_labels=True)
plt.savefig("figure10_18_1.png")
A=B/np.tile(B.sum(axis=1,keepdims=True),(1,B.shape[1]))
A=0.15/B.shape[0]+0.85*A  #计算状态转移概率矩阵
print("A=",A)
W,V=eigs(A.T,1); V=V.real
V=V.flatten(); #展开成（n,)形式的数组
V=V/V.sum(); print("V=",V); plt.figure(2)
plt.bar(range(1,B.shape[0]+1),V, width=0.6, color='b')
plt.savefig("figure10_18_2.png"); plt.show()
