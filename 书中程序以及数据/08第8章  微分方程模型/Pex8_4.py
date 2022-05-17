#程序文件Pex8_4.py
from scipy.integrate import odeint
from numpy import arange
dy=lambda y, x: -2*y+x**2+2*x
x=arange(1, 10.5, 0.5)
sol=odeint(dy, 2, x)
print("x={}\n对应的数值解y={}".format(x, sol.T))
