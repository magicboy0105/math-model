#程序文件Pex2_34.py
import numpy as np
from matplotlib.pyplot import *
x=np.linspace(0,2*np.pi,200)
y1=np.sin(x); y2=np.cos(x); y3=np.sin(x*x); y4=x*np.sin(x)
rc('font',size=16); rc('text', usetex=True)  #调用tex字库
ax1=subplot(2,3,1)  #新建左上1号子窗口
ax1.plot(x,y1,'r',label='$sin(x)$') #画图
legend()  #添加图例
ax2=subplot(2,3,2)  #新建2号子窗口
ax2.plot(x,y2,'b--',label='$cos(x)$'); legend() 
ax3=subplot(2,3,(3,6))  #3、6子窗口合并
ax3.plot(x,y3,'k--',label='$sin(x^2)$'); legend()
ax4=subplot(2,3,(4,5))  #4、5号子窗口合并
ax4.plot(x,y4,'k--',label='$xsin(x)$'); legend()
savefig('figure2_44.png',dpi=500); show()
