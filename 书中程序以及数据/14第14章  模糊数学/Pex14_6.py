#程序文件Pex14_6.py
import numpy as np
a=np.array([0.3,0.35,0.1]); aa=np.tile(a,(len(a),1)) 
b=np.array([[0.3,0.5,0.2],[0.2,0.2,0.4],[0.3,0.4,0.2]])
c=np.minimum(aa.T,b)  #两个矩阵的元素对应取最小值
T=c.max(axis=0)  #矩阵逐列取最大值
print("T=",T)

