#程序文件Pex6_4.py
from scipy.optimize import minimize
from numpy import ones
def obj(x):
    x1,x2,x3=x
    return (2+x1)/(1+x2)-3*x1+4*x3
LB=[0.1]*3; UB=[0.9]*3
bound=tuple(zip(LB, UB))   #生成决策向量界限的元组
res=minimize(obj,ones(3),bounds=bound) #第2个参数为初值
print(res.fun,'\n',res.success,'\n',res.x)  #输出最优值、求解状态、最优解
