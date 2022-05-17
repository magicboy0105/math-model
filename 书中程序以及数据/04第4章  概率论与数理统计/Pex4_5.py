#程序文件Pex4_5.py
from scipy.integrate import quad
from numpy import exp, sqrt, pi, abs
a=80; b=0.02; BD=a/b; mu=4000; s=100
y=lambda x: x*exp(-(x-mu)**2/(2*s**2))/sqrt(2*pi)/s   #定义积分的被积函数
I=0; x1=0; x2=10000
while abs(I-BD)>1E-16:
    c=(x1+x2)/2
    I=quad(y,-10000,c)[0] #由3sigma准则这里积分下限取为-10000,取零效果一样
    if I>BD: x2=c
    else: x1=c
print("最佳更换周期为：", c)
