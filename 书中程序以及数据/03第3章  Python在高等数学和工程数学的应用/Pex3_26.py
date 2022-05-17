#程序文件Pex3_26.py
import sympy as sp
A=sp.Matrix([[1],[2],[3]])  #列向量,即3×1矩阵
B=sp.Matrix([[4],[5],[6]])  
print("A的模为：",A.norm())
print("A的模的浮点数为：",A.norm().evalf())
print("A的转置矩阵为：",A.T)
print("A和B的点乘为：",A.dot(B))
print("A和B的叉乘为：",A.cross(B))
