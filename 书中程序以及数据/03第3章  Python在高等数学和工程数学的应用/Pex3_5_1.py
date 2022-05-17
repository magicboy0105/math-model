#程序文件Pex3_5_1.py
from pylab import rc
from sympy import plot_implicit as pt,Eq
from sympy.abc import x,y   #引进符号变量x,y
rc('font',size=16); rc('text',usetex=True)
pt(Eq((x-1)**2+(y-2)**3,4),(x,-6,6),(y,-2,4),xlabel='$x$',ylabel='$y$')
