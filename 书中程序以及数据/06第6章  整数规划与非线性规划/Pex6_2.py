#程序文件Pex6_2.py
import cvxpy as cp
import numpy as np
c=np.array([[4, 8, 7, 15, 12],
            [7, 9, 17, 14, 10],
            [6, 9, 12, 8, 7],
            [6, 7, 14, 6, 10],
            [6, 9, 12, 10, 6]])
x = cp.Variable((5,5),integer=True)
obj = cp.Minimize(cp.sum(cp.multiply(c,x)))
con= [0 <= x, x <= 1, cp.sum(x, axis=0, keepdims=True)==1,
               cp.sum(x, axis=1, keepdims=True)==1]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
