#程序文件Pex15_2.py
import numpy as np
import sympy as sp
from matplotlib.pyplot import plot,show,rc,legend,xticks
rc('font',size=16); rc('font',family='SimHei')
x0=np.array([25723,30379,34473,38485,40514,42400,48337])
n=len(x0); jibi=x0[:-1]/x0[1:]  #求级比
bd1=[jibi.min(),jibi.max()]    #求级比范围
bd2=[np.exp(-2/(n+1)),np.exp(2/(n+1))]   #q求级比的容许范围
x1=np.cumsum(x0)  #求累加序列
z=(x1[:-1]+x1[1:])/2.0
B=np.vstack([-z,np.ones(n-1)]).T
u=np.linalg.pinv(B)@x0[1:] #最小二乘法拟合参数

sp.var('t'); sp.var('x',cls=sp.Function)  #定义符号变量和函数
eq=x(t).diff(t)+u[0]*x(t)-u[1]  #定义符号微分方程
xt=sp.dsolve(eq,ics={x(0):x0[0]})  #求解符号微分方程
xt=xt.args[1]  #提取方程中的符号解
xt=sp.lambdify(t,xt,'numpy')  #转换为匿名函数
t=np.arange(n+1)
xt1=xt(t)  #求模型的预测值 
x0_pred=np.hstack([x0[0],np.diff(xt1)]) #还原数据
x2002=x0_pred[-1]  #提取2002年的预测值
cha=x0-x0_pred[:-1]; delta=np.abs(cha/x0)*100
print('1995~2002的预测值：',x0_pred)
print('\n-------------------\n','相对误差',delta)
t0=np.arange(1995,2002); plot(t0,x0,'*--')
plot(t0,x0_pred[:-1],'s-'); legend(('实际值','预测值'));
xticks(np.arange(1995,2002)); show()
