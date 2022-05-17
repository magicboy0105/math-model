#程序文件Pex8_10_2.py
import numpy as np
d=np.loadtxt("Pdata8_10_2.txt")  #加载文件中的数据
t0=d[0]; x0=d[1]  #提取年代数据及对应的人口数据
b=np.diff(x0)/10/x0[:-1]  #构造线性方程组的常数项列
a=np.vstack([np.ones(len(x0)-1),-x0[:-1]]).T #构造线性方程组系数矩阵
rs=np.linalg.pinv(a)@b;  r=rs[0]; xm=r/rs[1]
print("人口增长率r和人口最大值xm的拟合值分别为", np.round([r,xm],4))
xhat=xm/(1+(xm/3.9-1)*np.exp(-r*(2010-1790)))  #求预测值
print("2010年的预测值为：",round(xhat,4))

