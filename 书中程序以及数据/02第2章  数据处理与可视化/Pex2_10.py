#程序文件Pex2_10.py
import numpy as np
a=np.arange(4).reshape(2,2)  #生成数组[[0,1],[2,3]]
b=np.arange(4).reshape(2,2)  #生成数组[[0,1],[2,3]]
print(a.reshape(4,),'\n',a)  #输出：[0 1 2 3]和[[0,1],[2,3]]
print(b.resize(4,),'\n',b)   #输出：None和[0 1 2 3]
