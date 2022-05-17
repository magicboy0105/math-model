#程序文件Pex1_4.py
from math import *   #加载数学模块math的所有对象
n=0; x1=float(input("请输入角度："))
x=radians(x1)
s=a=x
while abs(a)>=1e-6:
    a *= -x*x/(2*n+3)/(2*n+2)
    n +=1; s += a
print("x={},sin(x)={}".format(x1,s))
