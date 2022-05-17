#程序文件Pex13_2.py
import sympy as sp
sp.var('k'); sp.var('y',cls=sp.Function)
f = y(k+1)-y(k)-3-2*k
f1 = sp.rsolve(f, y(k)); f2 = sp.simplify(f1)
print(f2)
       
