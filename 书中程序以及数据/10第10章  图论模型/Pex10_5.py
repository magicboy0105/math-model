#程序文件Pex10_5.py
import numpy as np
inf=np.inf
def Dijkstra_all_minpath( matr,start): #matr为邻接矩阵的数组，start表示起点
    n=len( matr) #该图的节点数
    dis=[]; temp=[]
    dis.extend(matr[start])  #添加数组matr的start行元素
    temp.extend(matr[start]) #添加矩阵matr的start行元素
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while len(visited)<n:
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        for j in range(n):
            if j not in visited:
                if (dis[i]+ matr[i][j])<dis[j]:
                    dis[j] = temp[j] =dis[i]+ matr[i][j]
                    parent[j]=i  #说明父节点是i
        visited.append(i)  #该索引已经处理了
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
    return dis
a=[[0,1,2,inf,7,inf,4,8],[1,0,2,3,inf,inf,inf,7],
  [2,2,0,1,5,inf,inf,inf],[inf,3,1,0,3,6,inf,inf],
  [7,inf,5,3,0,4,3,inf],[inf,inf,inf,6,4,0,6,4],
  [4,inf,inf,inf,3,6,0,2],[8,7,inf,inf,inf,4,2,0]]
d=Dijkstra_all_minpath(a,3)
print("v3到所有顶点的最短距离为：",d)
