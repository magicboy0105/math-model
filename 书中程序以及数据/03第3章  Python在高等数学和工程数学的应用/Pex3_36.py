#程序文件Pex3_36.py
import numpy as np
import numpy.linalg as LA
A=np.array([[2, 1, -5, 1],[1, -3, 0, -6],[0, 2, -1, 2],[1, 4, -7, 6]])
b=np.array([[8, 6, -2, 2]]); b=b.reshape(4,1)
print("系数矩阵A的秩为：",LA.matrix_rank(A))
print("线性方程组的唯一解为：",LA.inv(A).dot(b))   #使用逆矩阵
print("线性方程组的唯一解为：",LA.pinv(A).dot(b))  #使用伪逆
print("线性方程组的唯一解为：",LA.solve(A,b))  #利用solve求解
