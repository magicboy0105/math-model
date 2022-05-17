#程序文件Pex4_10.py
import numpy as np
import matplotlib.pyplot as plt
a=np.loadtxt("Pdata4_6_2.txt")
h=a[:,::2]; w=a[:,1::2]
h=np.reshape(h,(-1,1)); w=np.reshape(w,(-1,1))
hw=np.hstack((h,w)); plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.boxplot(hw,labels=['身高','体重'])
plt.savefig("figure4_10.png",dpi=500); plt.show()
