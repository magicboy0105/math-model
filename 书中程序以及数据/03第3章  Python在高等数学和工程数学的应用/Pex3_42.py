#程序文件Pex3_42.py
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
t = np.arange(8)
y=np.array([27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8]) 
A = np.c_[t, np.ones_like(t)]
ab = LA.lstsq(A, y, rcond=None)[0]  #返回值为向量
print(ab); plt.rc('font',size=16)
plt.plot(t, y, 'o', label='Original data', markersize=5)
plt.plot(t, A.dot(ab), 'r', label='Fitted line')
plt.legend(); plt.savefig("figure3_42.png",dpi=500); plt.show()
