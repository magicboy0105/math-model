#程序文件Pex3_2.py
from sympy import *
x1,x2,x3,x4=symbols('m1:5'); x=symbols('x')
print(x1/x2+x3/x4)
print(together(x1/x2+x3/x4))
print((2*x**2+3*x+4)/(x+1))
print(simplify((2*x**2+3*x+4)/(x+1)))  #化简没有效果
print(apart((2*x**2+3*x+4)/(x+1)))
