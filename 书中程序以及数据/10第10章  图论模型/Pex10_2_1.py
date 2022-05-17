#程序文件Pex10_2_1.py
import numpy as np
import networkx as nx
import pylab as plt
a=np.zeros((5,5))
a[0,1:5]=[9, 2, 4, 7]; a[1,2:4]=[3,4]
a[2,[3,4]]=[8, 4]; #输入邻接矩阵的上三角元素
a[3,4]=6; print(a); np.savetxt("Pdata10_2.txt",a) #保存邻接矩阵供以后使用
i,j=np.nonzero(a)  #提取顶点的编号
w=a[i,j]  #提出a中的非零元素
edges=list(zip(i,j,w))
G=nx.Graph()
G.add_weighted_edges_from(edges)
key=range(5); s=[str(i+1) for i in range(5)]
s=dict(zip(key,s))  #构造用于顶点标注的字符字典
plt.rc('font',size=18)
plt.subplot(121); nx.draw(G,font_weight='bold',labels=s)
plt.subplot(122); pos=nx.shell_layout(G)  #布局设置
nx.draw_networkx(G,pos,node_size=260,labels=s)
w = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,font_size=12,edge_labels=w) #标注权重
plt.savefig("figure10_2.png", dpi=500); plt.show()
