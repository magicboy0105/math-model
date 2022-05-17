#程序文件Pex4_21.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
a=np.loadtxt("Pdata4_6_2.txt")
w=a[:,1::2]; w=w.flatten()
mu=w.mean(); s=w.std(ddof=1)  #计算样本均值和标准差
print("均值和标准差分别为：", (mu, s))
statVal, pVal=ss.kstest(w,'norm',(mu,s))
print("统计量和P值分别为：", [statVal, pVal])
