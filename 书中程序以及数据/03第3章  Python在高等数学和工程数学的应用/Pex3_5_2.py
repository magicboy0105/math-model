#程序文件Pex3_5_2.py
from sympy import plot_implicit as pt
from sympy.abc import x,y   #引进符号变量x,y
ezplot=lambda expr:pt(expr)
ezplot((x-1)**2+(y-2)**3-4)
