#程序文件Pex10_17.py
import numpy as np
import networkx as nx
L=[(1,2,5,3),(1,3,3,6),(2,4,2,8),(3,2,1,2),(3,5,4,2),
   (4,3,1,1),(4,5,3,4),(4,6,2,10),(5,6,5,2)]
G=nx.DiGraph()
for k in range(len(L)):
    G.add_edge(L[k][0]-1,L[k][1]-1, capacity=L[k][2], weight=L[k][3])
mincostFlow=nx.max_flow_min_cost(G,0,5)
print("所求流为：",mincostFlow)
mincost=nx.cost_of_flow(G, mincostFlow)
print("最小费用为：", mincost)
flow_mat=np.zeros((6,6),dtype=int)
for i,adj in mincostFlow.items():
    for j,f in adj.items():
        flow_mat[i,j]=f
print("最小费用最大流的邻接矩阵为：\n",flow_mat)

