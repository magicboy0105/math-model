#程序文件Pex13_7_1.py
import sympy as sp
a0,b0, c0=sp.symbols('a0 b0 c0')
n=sp.symbols('n',positive=True)
A=sp.Matrix([[1,1/2,0],[0,1/2,1],[0,0,0]])
if A.is_diagonalizable(): print("A的对角化矩阵为：\n",A.diagonalize())
else: print("A不能对角化")
P=A.diagonalize()[0]; D=A.diagonalize()[1]
x=P*D**n*(P.inv())*sp.Matrix([a0,b0,c0])
x=sp.simplify(x); print(x)


