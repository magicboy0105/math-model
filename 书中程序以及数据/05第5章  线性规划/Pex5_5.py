#程序文件Pex5_5.py
import numpy
from cvxopt import matrix, solvers
c=matrix([2.,1]); A=matrix([[-1.,1],[-1,-1],[1,-2],[0,-1]]).T
b=matrix([1.,-2,4,0]); Aeq=matrix([1.,2],(1,2)) #Aeq为行向量
beq=matrix(3.5); sol=solvers.lp(c,A,b,Aeq,beq)
print("最优解为：\n",sol['x'])
print("最优值为：",sol['primal objective'])
