#程序文件Pex2_38.py
import numpy as np
from matplotlib.pyplot import *
x=np.linspace(0,2*np.pi,200)
y1=np.sin(x); y2=np.cos(pow(x,2))
rc('font',size=16); rc('text', usetex=True)  #调用tex字库
plot(x,y1,'r',label='$sin(x)$',linewidth=2)  #Latex格式显示公式
plot(x,y2,'b--',label='$cos(x^2)$')
xlabel('$x$'); ylabel('$y$',rotation=0)
savefig('figure2_38.png',dpi=500); legend(); show()
