#程序文件Pex3_24.py
from numpy import exp,cos
from scipy.optimize import fmin
f=lambda x: exp(x)*cos(2*x)
x0=fmin(f,0)
print("极小点为：{}，极小值为：{}".format(x0,f(x0)))
