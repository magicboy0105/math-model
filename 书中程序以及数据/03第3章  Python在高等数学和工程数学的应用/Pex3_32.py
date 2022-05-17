#程序文件Pex3_32.py
from sympy import Matrix, diag
A=Matrix([[0, -2, 2],[-2, -3, 4], [2, 4, -3]])
if A.is_diagonalizable(): print("A的对角化矩阵为：",A.diagonalize())
else: print("A不能对角化")
