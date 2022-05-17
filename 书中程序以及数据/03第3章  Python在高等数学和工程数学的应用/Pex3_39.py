#程序文件Pex3_39.py
import numpy as np
from numpy.linalg import eig
A=np.array([[0, -2, 2],[-2, -3, 4], [2, 4, -3]])
values, vectors=eig(A)
print("A的特征值为：",values)
print("A的特征向量为：",vectors)
