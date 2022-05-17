#程序文件Pex3_3.py
from sympy.plotting import plot
from sympy.abc import x,pi   #引进符号变量x及常量pi
from sympy.functions import sin,cos
plot((2*sin(x),(x,-6,6)),(cos(x+pi/4),(x,-5,5)))
