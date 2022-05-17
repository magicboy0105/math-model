#程序文件Pex3_15.py
from sympy import *
x=symbols('x'); y=symbols('y',cls=Function)
eq1=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)
eq2=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)-x*exp(2*x)
print("初值问题的解为：{}".format(dsolve(eq1,y(x),ics={y(0):1,diff(y(x),x).subs(x,0):0})))
y2=dsolve(eq2,y(x),ics={y(0):1,y(2):0})
print("边值问题的解为：{}".format(y2))
