#程序文件Pex3_13.py
from sympy import *
x=symbols('x'); y=2*x**3-5*x**2+x
x0=solve(diff(y,x),x)   #求驻点
print("驻点的精确解为",x0)
print("驻点的浮点数表示为：",[x0[i].n() for i in range(len(x0))])  #列表中的符号数无法整体转换为浮点数
y0=[y.subs(x,0),y.subs(x,1),y.subs(x,x0[0]).n()] #代入区间端点和一个驻点的值
print("三个点的函数值分别为:",y0)
