#程序文件Pex8_1.py
from sympy.abc import x
from sympy import diff, dsolve, simplify, Function
y=Function('y')
eq=diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)  #定义方程
con={y(0): 0, diff(y(x),x).subs(x,0): 1}  #定义初值条件
y=dsolve(eq, ics=con)
print(simplify(y))
