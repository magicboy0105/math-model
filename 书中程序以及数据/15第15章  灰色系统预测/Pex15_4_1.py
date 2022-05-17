#程序文件Pex15_4_1.py
import numpy as np
from sympy import Function, diff, dsolve, symbols, solve,exp
x0=np.array([41, 49, 61, 78, 96, 104])
n=len(x0); x1=np.cumsum(x0)  #计算1次累加序列
ax0=np.diff(x0)  #计算一次累减序列
z=0.5*(x1[1:]+x1[:-1])  #计算均值生成序列
B=np.c_[-x0[1:],-z,np.ones((n-1,1))]
u=np.linalg.pinv(B).dot(ax0)
p=np.r_[1,u[:-1]]  #构造特征多项式
r=np.roots(p)  #求特征根
xts=u[2]/u[1]  #常微分方程的特解
c1,c2,t=symbols('c1,c2,t'); eq1=c1+c2+xts-41;
eq2=c1*np.exp(5*r[0])+c2*np.exp(5*r[1])+xts-429
c=solve([eq1,eq2],[c1,c2])
s=c[c1]*exp(r[0]*t)+c[c2]*exp(r[1]*t)+xts  #微分方程的符号解
xt1=[]
for i in range(6): xt1.append(s.subs({t:i}))
xh0=np.r_[xt1[0],np.diff(xt1)]
cha=x0-xh0  #计算残差
delta=np.abs(cha)/x0  #计算相对误差
print(xt1,'\n------------\n',xh0,'\n------------\n',
      cha,'\n--------------\n',delta)
