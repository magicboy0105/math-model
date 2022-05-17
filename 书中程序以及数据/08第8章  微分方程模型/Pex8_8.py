#程序文件Pex8_8.py
import sympy as sp
sp.var('h')  #定义符号变量
sp.var('t', cls=sp.Function)  #定义符号函数
g = 9.8
eq = t(h).diff(h) -10000*sp.pi/0.62/sp.sqrt(2*g)*(h**(3/2)-2*h**(1/2))  #定义方程
t = sp.dsolve(eq, ics={t(1): 0}) #求微分方程的符号解
t = sp.simplify(t)
print(t.args[1].n(9))
