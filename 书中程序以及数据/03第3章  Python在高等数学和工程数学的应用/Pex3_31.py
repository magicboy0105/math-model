#程序文件Pex3_31.py
import sympy as sp
A=sp.Matrix([[0, -2, 2],[-2, -3, 4], [2, 4, -3]])
print("A的特征值为：",A.eigenvals())
print("A的特征向量为：",A.eigenvects())
