#程序文件Pex3_14.py
from sympy import *
x=symbols('x'); y=symbols('y',cls=Function)
eq1=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)
eq2=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)-x*exp(2*x)
print("齐次方程的解为：",dsolve(eq1,y(x)))
print("非齐次方程的解为：",dsolve(eq2,y(x)))
