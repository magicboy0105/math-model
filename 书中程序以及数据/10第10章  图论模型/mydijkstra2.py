import numpy as np
inf=np.inf
def Dijkstra_all_minpath(matrix,start):
    n=len(matrix)#该图的节点数
    path_array=[]
    temp=[]
    path_array.extend(matrix[start])  #深复制
    temp.extend(matrix[start])        #深复制
    temp[start] = inf  #临时数组会把处理过的节点的值变成inf，表示不是最小权值的节点了
    visited=[start]  #start已处理
    parent=[start]*n   #用于画路径，记录此路径中该节点的父节点
    while(len(visited)<n):
        i= temp.index(min(temp)) #找最小权值的节点的坐标
        temp[i]=inf
        path=[]  #用于画路径
        path.append(str(i))
        k=i
        while(parent[k]!=start):  #找该节点的父节点添加到path，直到父节点是start
            path.append(str(parent[k]))
            k=parent[k]
        path.append(str(start))
        path.reverse()   #path反序产生路径
        print(str(i)+':','->'.join(path))  #打印路径
        visited.append(i)  #该索引已经处理了
        for j in range(n):
            if j not in visited:
                if (path_array[i]+matrix[i][j])<path_array[j]:
                    path_array[j] = temp[j] =path_array[i]+matrix[i][j]
                    parent[j]=i  #说明父节点是i
    return path_array
 
#领接矩阵
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]

d=Dijkstra_all_minpath(a,0)
print("计算结果为：\n")
print(d)
