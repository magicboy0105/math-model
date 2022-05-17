#程序文件Pex2_39.py
import numpy as np
from matplotlib.pyplot import *
x=np.linspace(0,2*np.pi,200)
y1=np.sin(x); y2=np.cos(x); y3=np.sin(x*x)
rc('font',size=16); rc('text', usetex=True)  #调用tex字库
ax1=subplot(2,2,1)  #新建左上1号子窗口
ax1.plot(x,y1,'r',label='$sin(x)$') #画图
legend()  #添加图例
ax2=subplot(2,2,2)  #新建右上2号子窗口
ax2.plot(x,y2,'b--',label='$cos(x)$'); legend() 
ax3=subplot(2,1,2)  #新建两行、1列的下面子窗口
ax3.plot(x,y3,'k--',label='$sin(x^2)$'); legend(); 
savefig('figure2_39.png',dpi=500); show()
