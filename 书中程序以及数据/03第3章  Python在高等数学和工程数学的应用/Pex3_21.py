#程序文件Pex3_21.py
import numpy as np
from scipy.optimize import fsolve

def binary_search(f, eps, a, b):  #二分法函数
    c=(a+b)/2
    while np.abs(f(c))>eps:
        if f(a)*f(c)<0: b=c
        else: a=c
        c=(a+b)/2
    return c

def newton_iter(f, eps, x0, dx=1E-8):  #牛顿迭代法函数
    def diff(f, dx=dx):   #求数值导数函数
        return lambda x: (f(x+dx)-f(x-dx))/(2*dx)
    df=diff(f,dx)
    x1=x0-f(x0)/df(x0)
    while np.abs(x1-x0)>=eps:
        x1, x0=x1-f(x1)/df(x1), x1
    return x1

f=lambda x: x**3+1.1*x**2+0.9*x-1.4
print("二分法求得的根为：", binary_search(f,1E-6,0,1))
print("牛顿迭代法求得的根为：",newton_iter(f,1E-6,0))
print("直接调用SciPy求得的根为：",fsolve(f,0))
