#程序文件Pex2_40.py
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
ax=plt.axes(projection='3d')  #设置三维图形模式
z=np.linspace(0, 100, 1000)
x=np.sin(z)*z; y=np.cos(z)*z
ax.plot3D(x, y, z, 'k')
plt.savefig('figure2_40.png',dpi=500); plt.show()
