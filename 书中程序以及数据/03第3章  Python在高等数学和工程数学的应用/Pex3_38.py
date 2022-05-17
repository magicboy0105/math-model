#程序文件Pex3_38.py
from numpy import array
from numpy.linalg import pinv
A=array([[1, 1],[2, 2], [1, 2]])
b=array([1, 3, 2]); b.resize(3,1)
x=pinv(A).dot(b)  #求最小二乘解
print("最小二乘解为：",x)

