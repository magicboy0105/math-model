#程序文件Pex10_8.py
import numpy as np
import networkx as nx
a=np.loadtxt("Pdata10_6.txt")
G=nx.Graph(a)     #利用邻接矩阵构造赋权无向图
d=nx.shortest_path_length(G,weight='weight')  #返回值是可迭代类型
Ld=dict(d)  #转换为字典类型
print("顶点对之间的距离为：",Ld)  #显示所有顶点对之间的最短距离
print("顶点0到顶点4的最短距离为:",Ld[0][4])  #显示一对顶点之间的最短距离
m,n=a.shape; dd=np.zeros((m,n))
for i in range(m):
    for j in range(n): dd[i,j]=Ld[i][j]
print("顶点对之间最短距离的数组表示为：\n",dd)  #显示所有顶点对之间最短距离
np.savetxt('Pdata10_8.txt',dd) #把最短距离数组保存到文本文件中
p=nx.shortest_path(G, weight='weight')  #返回值是可迭代类型
dp=dict(p)  #转换为字典类型
print("\n顶点对之间的最短路径为：", dp)
print("顶点0到顶点4的最短路径为：",dp[0][4])
