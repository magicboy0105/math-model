#程序文件Pex8_3_2.py
import sympy as sp
t=sp.symbols('t')
x1,x2,x3=sp.symbols('x1:4',cls=sp.Function)
x=sp.Matrix([x1(t),x2(t),x3(t)])
A=sp.Matrix([[2,-3,3],[4,-5,3],[4,-4,2]])
eq=x.diff(t)-A*x
s=sp.dsolve(eq,ics={x1(0):1,x2(0):2,x3(0):3})
print(s)
