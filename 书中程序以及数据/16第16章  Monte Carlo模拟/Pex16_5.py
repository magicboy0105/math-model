#程序文件Pex16_5.py
from numpy.random import rand
import numpy as np
N=1000000; x=rand(N); y=rand(N)
n=np.sum(x**2+y**2<1)
s=4*n/N; print(s)


