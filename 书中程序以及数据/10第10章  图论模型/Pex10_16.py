#程序文件Pex10_16.py
import numpy as np
import networkx as nx
import pylab as plt
L=[(1,2,5),(1,3,3),(2,4,2),(3,2,1),(3,5,4),
   (4,3,1),(4,5,3),(4,6,2),(5,6,5)]
G=nx.DiGraph()
for k in range(len(L)):
    G.add_edge(L[k][0]-1,L[k][1]-1, capacity=L[k][2])
value, flow_dict= nx.maximum_flow(G, 0, 5)
print("最大流的流量为：",value)
print("最大流为：", flow_dict)
n = len(flow_dict)
adj_mat = np.zeros((n, n), dtype=int)
for i, adj in flow_dict.items():
    for j, weight in adj.items():
        adj_mat[i,j] = weight
print("最大流的邻接矩阵为：\n",adj_mat)
ni,nj=np.nonzero(adj_mat)  #非零弧的两端点编号
key=range(n)
s=['v'+str(i+1) for i in range(n)]
s=dict(zip(key,s)) #构造用于顶点标注的字符字典
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w=nx.get_edge_attributes(G,'capacity')
nx.draw(G,pos,font_weight='bold',labels=s,node_color='r')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(ni,nj))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            edge_color='r',width=3)
plt.show()
