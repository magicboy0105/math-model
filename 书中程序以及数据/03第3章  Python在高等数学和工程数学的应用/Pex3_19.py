#程序文件Pex3_19.py
import numpy as np
from scipy.integrate import dblquad

f1=lambda y, x: x*y**2  #第一个被积函数
print("I1：",dblquad(f1, 0, 2, 0, 1))

f2=lambda y, x: np.exp(-x**2/2)*np.sin(x**2+y)
bd=lambda x: np.sqrt(1-x**2)
print("I2:",dblquad(f2, -1, 1, lambda x: -bd(x), bd))
