# 程序文件Pex5_1.py
from scipy.optimize import linprog

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
bound = ((None, None), (-3, None))
res = linprog(c, A, b, None, None, bound)
print("目标函数的最小值：", res.fun)
print("最优解为：", res.x)
