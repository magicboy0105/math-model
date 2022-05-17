#程序文件Pex4_8.py
import numpy as np
import matplotlib.pyplot as plt
a=np.loadtxt("Pdata4_6_2.txt")
h=a[:,::2]; w=a[:,1::2]
h=np.reshape(h,(-1,1)); w=np.reshape(w,(-1,1))
plt.rc('font',size=16); plt.rc('font',family="SimHei")
plt.subplot(121); plt.xlabel("身高"); plt.hist(h,10) #只画直方图不返回频数表
plt.subplot(122); ps=plt.hist(w,6)  #画图并返回频数表ps
plt.xlabel("体重"); print("体重的频数表为：", ps)
plt.savefig("figure4_8.png", dpi=500); plt.show()
