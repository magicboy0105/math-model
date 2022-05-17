#程序文件Pex3_1.py
from sympy import *
x,y,z=symbols('x  y  z')
m0,m1,m2,m3=symbols('m0:4')  #创建多个符号变量
x=sin(1)
print("x=",x); print("x=",x.evalf())
print("x=",x.n(16))  #显示小数点后16位数字
print("pi的两种显示格式:{},{}".format(pi,pi.evalf(3)))  #这里不能使用n()函数
expr1=y*sin(y**2)  #创建第一个符号表达式
expr2=y**2+sin(y)*cos(y)+sin(z)  #创建第二个符号表达式
print("expr1=",expr1)
print("y=5时，expr1=",expr1.subs(y,5))  #代入一个符号变量的值
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}))  #代入y=2,z=3
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}).n())  #以浮点数显示计算结果
