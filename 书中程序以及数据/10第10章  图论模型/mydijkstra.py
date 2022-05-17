#程序文件Pex10_12.py
import numpy as np
inf=np.inf


def dijkstra(a,sb,db):
    n=len(a); visit=[0]*n
    dis=[inf]*n; dis[0]=0
    visit[sb]=1; u=sb  #u为最新的P标号顶点
    parent=[0]*n  #前驱顶点的初始化
    for i in range(n):
        id=[index for index,value in enumerate(visit) if value==0]  #查找未标号的顶点
        for v in id:
            if a[u,v]+dis[u]<dis[v]:
                dis[v]=dis[u]+a[u][v]
                parent[v]=u
        temp=dis
        temp[visit==1]=inf  #已标号点的距离换成无穷
        t=np.min(temp); u=temp.index(t)  #找标号值最小的顶点
        visit[u]=1  #标记已经标号的顶点
        mypath=[]
        if parent[db]!=0:  #存在路
            t=db; mypath=[db]
            while t!=sb:
                p=parent[t]; mypath.insert(0,p); t=p
#return dis[db], mypath
a=[[0,50,inf,40,25,10],[50,0,15,20,inf,25],
   [inf,15,0,10,20,inf],[40,20,10,0,10,25],
   [25,inf,20,10,0,55],[10,25,inf,25,55,0]]
path,distance=dijkstra(a,1,3)
         

            
            
            
    

