#程序文件Pex3_40.py
from numpy import array, dot
from numpy.linalg import eig,inv
A=array([[0, -2, 2],[-2, -3, 4], [2, 4, -3]])
values, vectors=eig(A)
check=dot(inv(vectors),A).dot(vectors)
print("check=\n", check)
