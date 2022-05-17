#程序文件Pex2_3.py
import numpy as np  
a=np.linspace(0,2,5)   #生成数组：[0., 0.5, 1., 1.5, 2.]
b=np.mgrid[0:2:5j]     #等价于np.linspace(0,2,5)
x,y=np.mgrid[0:2:4j,10:20:5j]  #生成[0,2]×[10,20]上的4×5的二维数组
print("x={}\ny={}".format(x,y))
