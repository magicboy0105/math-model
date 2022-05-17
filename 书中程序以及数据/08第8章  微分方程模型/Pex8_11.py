#程序文件Pex8_11.py
import sympy as sp
sp.var('t',positive=True); sp.var('s')  #定义符号变量
sp.var('Y',cls=sp.Function)  #定义符号函数
g=4*t*sp.exp(t)
Lg=sp.laplace_transform(g,t,s)  #方程右端项的拉氏变换
d=s**4*Y(s)+2*s**2*Y(s)+Y(s)
de=d-Lg[0]    #定义取拉氏变换后的代数方程
Ys=sp.solve(de,Y(s))[0]  #求像函数
Ys=sp.factor(Ys)
yt=sp.inverse_laplace_transform(Ys,s,t)
print("y(t)=",yt); yt=yt.rewrite(sp.exp)
#这里的变换只是为了把解化成指数函数，并且不出现虚数
yt=yt.as_real_imag(); print("y(t)=",yt)
yt=sp.simplify(yt[0]); print("y(t)=",yt)
