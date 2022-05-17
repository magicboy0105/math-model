#程序文件Pex8_7.py
import sympy as sp
sp.var('t, k')  #定义符号变量t,k
u = sp.var('u', cls=sp.Function)  #定义符号函数
eq = sp.diff(u(t), t) + k * (u(t) - 24)  #定义方程
uu = sp.dsolve(eq, ics={u(0): 150}) #求微分方程的符号解
print(uu)
kk = sp.solve(uu, k)  #kk返回值是列表，可能有多个解
k0 = kk[0].subs({t: 10.0, u(t): 100.0})
print(kk, '\t', k0)
u1 = uu.args[1]  #提出符号表达式
u0 = u1.subs({t: 20, k: k0})  #代入具体值
print("20分钟后的温度为：", u0)
