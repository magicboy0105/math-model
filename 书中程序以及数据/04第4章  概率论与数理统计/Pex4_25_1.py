#程序文件Pex4_25_1.py
import matplotlib.pyplot as plt
import numpy as np
x=[2.5, 3.9, 2.9, 2.4, 2.9, 0.8, 9.1, 0.8, 0.7,7.9, 1.8, 1.9, 0.8, 6.5, 1.6, 5.8, 1.3, 1.2, 2.7]
y=[211, 167, 131, 191, 220, 297, 71, 211, 300, 107,
   167, 266, 277, 86, 207, 115, 285, 199, 172]
plt.plot(x,y,'+k', label="原始数据点")
p=np.polyfit(x,y,deg=1)  #拟合一次多项式
print("拟合的多项式为:{}*x+{}".format(p[0],p[1]))
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.plot(x, np.polyval(p,x), label="拟合的直线")
print("预测值为：", np.polyval(p, 8)); plt.legend()
plt.savefig("figure4_25.png", dpi=500); plt.show()
