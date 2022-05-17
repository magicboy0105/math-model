#程序文件Pex2_12.py
import numpy as np
a=np.arange(4).reshape(2,2)  #生成数组[[0,1],[2,3]]
b=np.arange(4,8).reshape(2,2)  #生成数组[[4,5],[6,7]]
c1=np.vstack([a,b])  #垂直方向组合
c2=np.r_[a,b]        #垂直方向组合
d1=np.hstack([a,b])  #水平方向组合
d2=np.c_[a,b]        #水平方向组合

