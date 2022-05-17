#程序文件Pz13_1.py
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text',usetex=True); plt.rc('font',size=16)
logistic=lambda k, x: k*x*(1-x)
kk=np.arange(0, 4.01, 0.01); listk=[]; listx=[]
for k in kk:
    x=0.5
    for i in range(1,500):
        x1=logistic(k,x); x=x1
        if i>400: listk.append(k); listx.append(x)
plt.scatter(listk,listx,c='b',s=1); plt.grid(True)
plt.xticks(np.arange(0,4.01,0.5)); plt.xlabel("$k$")
plt.ylabel("$x^*(k)$"); plt.show()
