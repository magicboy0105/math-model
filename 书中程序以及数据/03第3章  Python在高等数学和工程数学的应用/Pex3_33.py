#程序文件Pex3_33.py
from numpy import arange, cross, inner 
from numpy.linalg import norm
a=arange(1,4); b=arange(4,7)       #创建数组
print("a的二范数为：",norm(a))
print("a点乘b=", a.dot(b))      #行向量a乘以列向量b
print("a,b的内积=",inner(a,b))  #a,b的内积,这里与dot(a,b)等价
print("a叉乘b=", cross(a,b))
