#程序文件Pex6_3_2.py
import cvxpy as cp
import numpy as np
L=np.array([48.7,52.0,61.3,72.0,48.7,52.0,64.0])
w=np.array([2000,3000,1000,500,4000,2000,1000])
a=np.array([8,7,9,6,6,4,8])
x=cp.Variable((2,7), integer=True)
obj=cp.Maximize(cp.sum(x*w))
con=[cp.sum(x,axis=0,keepdims=True)<=a.reshape(1,7),
     x*L<=1020, x*w<=40000, cp.sum(x[:,4:]*L[4:])<=302.7,x>=0]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI',verbose =True)
print("最优值为:",prob.value)
print("最优解为：\n",x.value)

