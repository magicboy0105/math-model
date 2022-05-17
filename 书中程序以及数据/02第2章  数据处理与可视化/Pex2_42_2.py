#程序文件Pex2_28_2.py
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
z=np.loadtxt("Pdata2_42.txt")  #加载高程数据
x=np.arange(0,1500,100)
y=np.arange(1200,-10,-100)
ax1=plt.subplot(1,2,1)
contr=plt.contour(x,y,z); plt.clabel(contr)  #画等高线并标注
plt.xlabel('$x$'); plt.ylabel('$y$',rotation=0)
ax2=plt.subplot(1,2,2,projection='3d')
plt.sca(ax2)
X,Y=np.meshgrid(x,y)
ax2.plot_surface(X, Y, z,cmap='viridis')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')
plt.savefig('figure2_42_2.png',dpi=500); plt.show()
