#程序文件py10_7.py
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
a=np.array([[0,1,2,inf,7,inf,4,8],[1,0,2,3,inf,inf,inf,7],
  [2,2,0,1,5,inf,inf,inf],[inf,3,1,0,3,6,inf,inf],
  [7,inf,5,3,0,4,3,inf],[inf,inf,inf,6,4,0,6,4],
  [4,inf,inf,inf,3,6,0,2],[8,7,inf,inf,inf,4,2,0]])  #输入邻接矩阵
dis, path=floyd(a)
print("所有顶点对之间的最短距离为：\n", dis, '\n',"路由矩阵为：\n",path)
