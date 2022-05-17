#程序文件py10_6.py
import numpy as np
def floyd(graph):
    m = len(graph)
    dis = graph
    path = np.zeros((m, m))  #路由矩阵初始化
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = k

    return dis, path
inf=np.inf
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]  #输入邻接矩阵
dis, path=floyd(a)
print("所有顶点对之间的最短距离为：\n", dis, '\n',"路由矩阵为：\n",path)
        
    


