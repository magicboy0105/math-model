#程序文件Pex3_37.py
from numpy import array
from numpy.linalg import pinv
A=array([[1, 1, -3, -1],[3, -1, -3, 4], [1, 5, -9, -8]])
b=array([1, 4, 0]); b.resize(3,1)
x=pinv(A).dot(b)  #求最小范数解
print("最小范数解为：",x)

