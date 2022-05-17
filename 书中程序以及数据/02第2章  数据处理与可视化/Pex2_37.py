#程序文件Pex2_37.py
import numpy as np
from matplotlib.pyplot import *
x=np.array(range(8))
y='27.0  26.8	  26.5	26.3	 26.1  25.7	 25.3	24.8'  #数据是粘贴过来的
y=",".join(y.split())    #把空格替换成逗号
y=np.array(eval(y))      #数据之间加逗号太麻烦，我们用程序转换
scatter(x,y)
savefig('figure2_23.png',dpi=500); show()
