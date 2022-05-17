#程序文件Pex3_25.py
from scipy.optimize import minimize
f=lambda x: 100*(x[1]-x[0]**2)**2+(1-x[0])**2; 
x0=minimize(f,[2.0, 2.0])
print("极小点为：{}，极小值为：{}".format(x0.x,x0.fun))
