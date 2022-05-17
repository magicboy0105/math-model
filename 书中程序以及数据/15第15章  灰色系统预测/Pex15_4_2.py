#程序文件Pex15_4_2.py
import numpy as np
import sympy as sp
x0=np.array([41,49,61,78,96,104])
n=len(x0)
lamda=x0[:-1]/x0[1:]  #计算级比
rang=[lamda.min(), lamda.max()]  #计算级比的范围
theta=[np.exp(-2/(n+1)),np.exp(2/(n+1))] #计算级比容许范围
x1=np.cumsum(x0)  #累加运算
z=0.5*(x1[1:]+x1[:-1])
B=np.vstack([-x0[1:],-z,np.ones(n-1)]).T
u=np.linalg.pinv(B)@np.diff(x0)  #最小二乘法拟合参数
print("参数u：",u)
sp.var('t'); sp.var('x',cls=sp.Function)  #定义符号变量和函数
eq=x(t).diff(t,2)+u[0]*x(t).diff(t)+u[1]*x(t)-u[2]
s=sp.dsolve(eq,ics={x(0):x0[0],x(5):x1[-1]})  #求微分方程符号解
xt=s.args[1]  #提取解的符号表达式
print('xt=',xt)
fxt=sp.lambdify(t,xt,'numpy')  #转换为匿名函数
yuce1=fxt(np.arange(n))  #求预测值
yuce=np.hstack([x0[0],np.diff(yuce1)])  #还原数据
epsilon=x0-yuce[:n]  #计算已知数据预测的残差
delta=abs(epsilon/x0)  #计算相对误差
print('相对误差：',np.round(delta*100,2))  #显示相对误差

