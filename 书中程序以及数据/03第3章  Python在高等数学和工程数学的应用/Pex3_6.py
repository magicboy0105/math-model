#程序文件Pex3_6.py
from sympy import *
x=symbols('x')
print(limit(sin(x)/x,x,0))
print(limit(pow(1+1/x,x),x,oo))  #这里是两个小”o”，表示正无穷
