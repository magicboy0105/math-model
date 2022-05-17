#程序文件Pex5_4.py
import numpy as np
from cvxopt import matrix, solvers
c=matrix([-4.,-5]); A=matrix([[2.,1],[1,2],[-1,0],[0,-1]]).T
b=matrix([3.,3,0,0]); sol=solvers.lp(c,A,b)
print("最优解为：\n",sol['x'])
print("最优值为：",sol['primal objective'])
