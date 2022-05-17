#程序文件Pex8_12.py
import sympy as sp
import pylab as plt
import numpy as np
sp.var('t',positive=True); sp.var('s')  #定义符号变量
sp.var('X,Y',cls=sp.Function)  #定义符号函数
g=40*sp.sin(3*t)
Lg=sp.laplace_transform(g,t,s)  
eq1=2*s**2*X(s)+6*X(s)-2*Y(s)
eq2=s**2*Y(s)-2*X(s)+2*Y(s)-Lg[0]
eq=[eq1,eq2]    #定义取拉氏变换后的代数方程组
XYs=sp.solve(eq,(X(s),Y(s)))  #求像函数
Xs=XYs[X(s)]; Ys=XYs[Y(s)]
Xs=sp.factor(Xs); Ys=sp.factor(Ys)
xt=sp.inverse_laplace_transform(Xs,s,t)
yt=sp.inverse_laplace_transform(Ys,s,t)
print("x(t)=",xt); print("y(t)=",yt)
fx=sp.lambdify(t,xt,'numpy')  #转换为匿名函数
fy=sp.lambdify(t,yt,'numpy')
t=np.linspace(-5,5,100)
plt.rc('text',usetex=True)
plt.plot(t,fx(t),'*-k',label='$x(t)$')
plt.plot(t,fy(t),'.-r',label='$y(t)$')
plt.xlabel('$t$'); plt.legend(); plt.show()
