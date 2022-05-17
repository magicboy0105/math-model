#程序文件Pex4_11.py
import numpy as np
import matplotlib.pyplot as plt
a=np.loadtxt("Pdata4_6_2.txt")
w=a[:,1::2]; w=np.reshape(w,(-1,1)); plt.rc('font',size=16)
h=plt.hist(w,20,density=True, histtype='step', cumulative=True)
print(h); plt.grid()
plt.savefig("figure4_11.png",dpi=500); plt.show()
