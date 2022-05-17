#程序文件Pex3_7.py
from sympy import *
x,y=symbols('x y')    #定义两个符号变量
z=sin(x)+x**2*exp(y)     #构造符号表达式
print("关于x的二阶偏导数为：",diff(z,x,2))
print("关于y的一阶偏导数为：",diff(z,y))
