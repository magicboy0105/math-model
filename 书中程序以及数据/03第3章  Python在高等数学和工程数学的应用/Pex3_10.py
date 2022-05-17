#程序文件Pex3_10.py
from sympy import integrate, symbols, sin, pi, oo
x=symbols('x')
print(integrate(sin(2*x),(x,0,pi)))
print(integrate(sin(x)/x,(x,0,oo)))
