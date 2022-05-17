#程序文件Pex3_22_2.py
from numpy import sin
from scipy.optimize import fsolve
def Pfun(x):
    x1,x2,x3=x.tolist()  #x转换成列表
    return 5*x2+3, 4*x1**2-2*sin(x2*x3), x2*x3-1.5
print("result=",fsolve(Pfun, [1.0, 1.0, 1.0]))
