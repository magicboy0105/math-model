#程序文件Pex12_8.py
import numpy as np
b=np.loadtxt("Pdata12_7_2.txt")
odds9=np.exp(np.dot(b,[1,9]))
odds9vs8=np.exp(np.dot([1,9],b))/np.exp(np.dot([1,8],b))
print("odds9=%.4f,odds9vs8=%.4f"%(odds9,odds9vs8))

