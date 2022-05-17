#程序文件Pex2_43.py
import matplotlib.pyplot as plt
from numpy import *
x=linspace(0,15,11); y=linspace(0,10,12)
x,y=meshgrid(x,y)  #生成网格数据
v1=y*cos(x); v2=y*sin(x)
plt.quiver(x,y,v1,v2)
plt.savefig('figure2_43.png',dpi=500); plt.show()
