#程序文件Pex3_27.py
import sympy as sp
import numpy as np
A=sp.Matrix(np.arange(1,17).reshape(4,4))
B=sp.eye(4)
print("A的行列式为：",sp.det(A))
print("A的秩为：",A.rank())
print("A的转置矩阵为：",A.transpose())  #等价于A.T
print("所求的逆阵为：",(A+10*B).inv())
print("A的平方为：",A**2)
print("A,B的乘积为：",A*B)
print("横连矩阵为：",A.row_join(B))
print("纵连矩阵为：",A.col_join(B))
print("A1为：",A[0:2,0:2])
A2=A.copy(); A2.row_del(3)
print("A2为：",A2)
