#程序文件Pex3_20.py
import numpy as np
from scipy.integrate import tplquad
f=lambda z, y, x: z*np.sqrt(x**2+y**2+1)
ybd=lambda x: np.sqrt(2*x-x**2)
print("I=",tplquad(f, 0, 2, lambda x: -ybd(x),ybd, 0, 6))
