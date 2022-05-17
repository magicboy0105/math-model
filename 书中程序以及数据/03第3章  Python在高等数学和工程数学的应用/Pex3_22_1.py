#程序文件Pex3_22_1.py
from numpy import sin
from scipy.optimize import fsolve
f=lambda x: [5*x[1]+3, 4*x[0]**2-2*sin(x[1]*x[2]), x[1]*x[2]-1.5]
print("result=",fsolve(f, [1.0, 1.0, 1.0]))
