#程序文件Pan6_6.py
import numpy as np
from cvxopt import matrix,solvers
n=3; P=matrix(0.,(n,n))
P[::n+1]=[3,2,1.7]; q=matrix([3,-8.2,-1.95])
A=matrix([[1.,0,1],[-1,2,0],[0,1,2]]).T
b=matrix([2.,2,3])
Aeq=matrix(1.,(1,n)); beq=matrix(3.)
s=solvers.qp(P,q,A,b,Aeq,beq)
print("最优解为：",s['x'])
print("最优值为：",s['primal objective'])

