#程序文件Pex3_18.py
import numpy as np
from scipy.integrate import quad

def trapezoid(f,n,a,b):    #定义梯形公式的函数
    xi=np.linspace(a,b,n); h=(b-a)/(n-1)
    return h*(np.sum(f(xi))-(f(a)+f(b))/2)

def simpson(f,n,a,b):     #定义辛普森公式的函数
    xi, h=np.linspace(a,b,2*n+1), (b-a)/(2.0*n)
    xe=[f(xi[i]) for i in range(len(xi)) if i%2==0]
    xo=[f(xi[i]) for i in range(len(xi)) if i%2!=0]
    return h*(2*np.sum(xe)+4*np.sum(xo)-f(a)-f(b))/3.0

a=0; b=1; n=1000
f=lambda x: np.sin(np.sqrt(np.cos(x)+x**2))

print("梯形积分I1=",trapezoid(f,n,a,b))
print("辛普森积分I2=",simpson(f,n,a,b))
print("SciPy积分I3=",quad(f,a,b))
