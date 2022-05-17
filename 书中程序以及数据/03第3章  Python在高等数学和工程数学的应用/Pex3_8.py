#程序文件Pex3_8.py
from sympy import *
k,n=symbols('k  n')
print(summation(k**2,(k,1,n)))
print(factor(summation(k**2,(k,1,n))))  #把计算结果因式分解
print(summation(1/k**2,(k,1,oo)))  #这里是两个小o表示正无穷
