#程序文件Pex3_12.py
from sympy.abc import x, y
from sympy import solve
s=solve([x**2+y**2-1, x-y], [x, y])
print("方程组的解为：", s)
