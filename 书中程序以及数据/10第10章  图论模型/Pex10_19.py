#程序文件Pex10_19.py
import numpy as np
import networkx as nx
L=[(1,2),(1,3),(2,3),(2,4),(2,5),(3,5),
   (4,5),(4,6)]
G=nx.Graph()   #构造无向图
G.add_nodes_from(range(1,7))  #添加顶点集
G.add_edges_from(L)
D=nx.diameter(G)  #求网络直径
LH=nx.average_shortest_path_length(G) #求平均路径长度
Ci=nx.clustering(G)   #求各顶点的聚类系数
C=nx.average_clustering(G)  #求整个网络的聚类系数
print("网络直径为：",D,"\n平均路径长度为：",LH)
print("各顶点的聚类系数为：")
for index,value in enumerate(Ci.values()):
    print("(顶点v{:d}: {:.4f})；".format(index+1,value),end=' ')
print("\n整个网络的聚类系数为：{:.4f}".format(C))
