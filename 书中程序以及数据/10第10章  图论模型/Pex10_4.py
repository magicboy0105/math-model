#程序文件Pex10_4.py
import numpy as np
import networkx as nx
import pylab as plt
a=np.loadtxt("Pdata10_2.txt")
G=nx.Graph(a)     #利用邻接矩阵构造赋权无向图
print("图的顶点集为：", G.nodes(),"\n边集为：", G.edges())
print("邻接表为：", list(G.adjacency()))  #显示图的邻接表
print("列表字典为：", nx.to_dict_of_lists(G)) 
B=nx.to_numpy_matrix(G)  #从图G中导出邻接矩阵B，这里B=a
C=nx.to_scipy_sparse_matrix(G)  #从图G中导出稀疏矩阵C
