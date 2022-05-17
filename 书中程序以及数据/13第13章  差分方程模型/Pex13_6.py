#程序文件Pex13_6.py
import numpy as np
from matplotlib.pyplot import rc, plot, show, legend, figure
rc('font',size=16); rc('font',family='SimHei')
a=np.loadtxt("Pdata13_6.txt"); 
plot(np.arange(0,19),a,'*'); show()
b=np.c_[a[:-1],-a[:-1]**2]
c=np.diff(a); x=np.linalg.pinv(b).dot(c)
r=x[0]; N=x[0]/x[1]
print("r,s,N的拟合值分别为：",r,'\t',x[1],'\t',N)
Tx=np.zeros(19); Tx[0]=9.6; x0=9.6
for i in range(1,19):
    xn=x0+r*x0*(1-x0/N)
    Tx[i]=xn; x0=xn
figure; plot(np.arange(0,19),a,'*')
plot(np.arange(19), Tx,'o-')
legend(("原始数据点","拟合值"), loc='best'); show()
delta=np.abs((Tx-a)/a);
print("所有已知点的预测值的相对误差",delta)
print("最大相对误差:",delta.max())

