#程序文件Pex3_17.py
import numpy as np, numpy.linalg as ng
import matplotlib.pyplot as plt
N=4; v=1.0; d=200.0; time=400.0; divs=201
xy=np.array([[-d,d],[d,d],[d,-d],[-d,-d]])
T=np.linspace(0,time,divs); dt=T[1]-T[0]
xyn=np.empty((4,2)); Txy=xy
for n in range(1,len(T)):
    for i in [0,1,2,3]:
        j=(i+1)%4; dxy=xy[j]-xy[i]
        dd=dxy/ng.norm(dxy) #单位化向量
        xyn[i]=xy[i]+v*dt*dd; #计算下一步的位置
    Txy=np.c_[Txy,xyn]; xy=xyn
for i in range(N):plt.plot(Txy[i,::2],Txy[i,1::2])
plt.savefig("figure3_17.png",dpi=500); plt.show()
