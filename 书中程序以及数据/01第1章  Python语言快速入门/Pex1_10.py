#程序文件Pex1_10.py
from math import log, exp, sin, pi
f=lambda n:(1+log(n)+sin(n))/(2*pi)
y=exp(2)
for n in range(1,101): y += f(n)
print("y=%7.4f"%y)
