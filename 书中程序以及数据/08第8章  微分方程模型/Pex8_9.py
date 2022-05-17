#程序文件Pex8_9.py
from numpy import array
v0=array([45, 65, 80])
T0=1; L=4.5; I=9; mu=0.7; g=9.8
T=v0/(2*mu*g)+(I+L)/v0+T0
print(T)

