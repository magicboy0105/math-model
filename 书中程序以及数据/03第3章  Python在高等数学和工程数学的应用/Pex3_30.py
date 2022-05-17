#程序文件Pex3_30.py
import sympy as sp
A=sp.Matrix([[1, 1, -3, -1],[3, -1, -3, 4], [1, 5, -9, -8]])
b=sp.Matrix([1, 4, 0]); b.transpose()
C=A.row_join(b)  #构造增广矩阵
print("增广阵的行最简形为：\n",C.rref())
