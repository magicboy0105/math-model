#程序文件Pex3_29.py
import sympy as sp
A=sp.Matrix([[1, -5, 2, -3],[5, 3, 6, -1], [2, 4, 2, 1]])
print("A的零空间（即基础解系）为：",A.nullspace())
