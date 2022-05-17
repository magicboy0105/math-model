#程序文件Pex2_2.py
import numpy as np
a=np.arange(4,dtype=float)  #创建浮点型数组：[0. 1. 2. 3.]
b=np.arange(0,10,2,dtype=int)  #创建整型数组：[0, 2, 4, 6, 8]
c=np.empty((2,3),int)   #创建2×3的整型空矩阵
d=np.linspace(-1,2,5)  #创建数组：[-1., -0.25,  0.5,  1.25,  2.]
e=np.random.randint(0,3,(2,3))  #生成[0,3)上的2行3列的随机整数数组
