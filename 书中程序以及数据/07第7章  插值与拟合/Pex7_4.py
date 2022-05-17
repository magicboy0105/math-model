#程序文件名Pex7_4.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d 
x=np.arange(0,25,2)
y=np.array([12, 9, 9, 10, 18, 24, 28, 27, 25, 20, 18, 15, 13])
xnew=np.linspace(0, 24, 500)  #插值点
f1=interp1d(x, y); y1=f1(xnew);
f2=interp1d(x, y,'cubic'); y2=f2(xnew)
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.subplot(121), plt.plot(xnew, y1); plt.xlabel("（A）分段线性插值")
plt.subplot(122); plt.plot(xnew, y2); plt.xlabel("（B）三次样条插值")
plt.savefig("figure7_4.png", dpi=500); plt.show()
