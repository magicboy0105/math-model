#程序文件名Pex7_6.py
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
x=np.array([129,140,103.5,88,185.5,195,105,157.5,107.5,77,81,162,162,117.5])
y=np.array([7.5,141.5,23,147,22.5,137.5,85.5,-6.5,-81,3,56.5,-66.5,84,-33.5])
z=-np.array([4,8,6,8,6,8,8,9,9,8,8,9,4,9])
xy=np.vstack([x,y]).T
xn=np.linspace(x.min(), x.max(), 100)
yn=np.linspace(y.min(), y.max(), 100)
xng, yng = np.meshgrid(xn,yn)  #构造网格节点
zn=griddata(xy, z, (xng, yng), method='nearest')  #最近邻点插值
plt.rc('font',size=16); plt.rc('text',usetex=True)
ax=plt.subplot(121,projection='3d'); 
ax.plot_surface(xng, yng, zn,cmap='viridis')
ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
plt.subplot(122); c=plt.contour(xn,yn,zn,8); plt.clabel(c)
plt.savefig('figure7_6.png',dpi=500); plt.show()
