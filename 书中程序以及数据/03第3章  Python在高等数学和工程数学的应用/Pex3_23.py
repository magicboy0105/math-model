#程序文件Pex3_23.py
from numpy import exp,cos
from scipy.optimize import fminbound
f=lambda x: exp(x)*cos(2*x)
x0=fminbound(f,0,3)
print("极小点为：{}，极小值为：{}".format(x0,f(x0)))
