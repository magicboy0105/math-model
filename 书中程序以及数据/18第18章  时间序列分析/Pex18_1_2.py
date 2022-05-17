#程序文件Pex18_1_2.py
import numpy as np
y=np.array([423,358,434,445,527,429,426,502,480,384,427,446])
n1=3; yt1=np.convolve(np.ones(n1)/n1,y)[n1-1:-n1+1]
s1=np.sqrt(((y[n1:]-yt1[:-1])**2).mean())
n2=5; yt2=np.convolve(np.ones(n2)/n2,y)[n2-1:-n2+1]
s2=np.sqrt(((y[n2:]-yt2[:-1])**2).mean())
print('N=3时,预测值：',yt1,'，预测的标准误差：',s1)
print('N=5时,预测值：',yt2,'，预测的标准误差：',s2)
