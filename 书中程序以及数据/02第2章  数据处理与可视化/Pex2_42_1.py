#程序文件Pex2_42_1.py
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
z=np.loadtxt("Pdata2_42.txt")  #加载高程数据
x=np.arange(0,1500,100)
y=np.arange(1200,-10,-100)
contr=plt.contour(x,y,z); plt.clabel(contr)  #画等高线并标注
plt.xlabel('$x$'); plt.ylabel('$y$',rotation=0)
plt.savefig('figure2_42_1.png',dpi=500)
plt.figure()  #创建一个绘图对象
ax=plt.axes(projection='3d') #用这个绘图对象创建一个三维坐标轴对象
X,Y=np.meshgrid(x,y)
ax.plot_surface(X, Y, z,cmap='viridis')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
plt.savefig('figure2_42_2.png',dpi=500); plt.show()
