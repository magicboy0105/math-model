#程序文件Pex13_1.py
from sympy import Function, rsolve
from sympy.abc import n
y = Function('y')
f=y(n+2)-y(n+1)-y(n)
ff=rsolve(f, y(n),{y(1):1,y(2):1})
print(ff)
