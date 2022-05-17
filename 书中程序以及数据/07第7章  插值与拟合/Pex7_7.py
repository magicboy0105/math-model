#程序文件名Pex7_7.py
from numpy import polyfit, polyval, array, arange
from matplotlib.pyplot import plot,show,rc
x0=arange(0, 1.1, 0.1)
y0=array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
p=polyfit(x0, y0, 2) #拟合二次多项式
print("拟合二次多项式的从高次幂到低次幂系数分别为:",p)
yhat=polyval(p,[0.25, 0.35]); print("预测值分别为：", yhat)
rc('font',size=16)
plot(x0, y0, '*', x0, polyval(p, x0), '-'); show()

