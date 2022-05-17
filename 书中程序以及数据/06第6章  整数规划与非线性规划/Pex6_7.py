#程序文件Pex6_7.py
import cvxpy as cp
import numpy as np
c1=np.array([1, 1, 3, 4, 2])
c2=np.array([-8, -2, -3, -1, -2])
a=np.array([[1, 1, 1, 1, 1], [1, 2, 2, 1, 6], [2, 1, 6, 0, 0], [0, 0, 1, 1, 5]])
b=np.array([400, 800, 200, 200])
x=cp.Variable(5,integer=True)
obj=cp.Minimize(c1*x**2+c2*x)
con=[0<=x, x<=99, a*x<=b]
prob = cp.Problem(obj, con)
prob.solve()
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
