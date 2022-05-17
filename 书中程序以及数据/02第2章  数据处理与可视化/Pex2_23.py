#程序文件Pex2_23.py
import numpy as np
a=np.arange(6).reshape(2,3)
np.save("Pdata2_23_1.npy",a)
b=np.load("Pdata2_23_1.npy")

c=np.arange(6,12).reshape(2,3)
d=np.sin(c)
np.savez("Pdata2_23_2.npz",c,d)
e=np.load("Pdata2_23_2.npz")
f1=e["arr_0"]  #提取第一个数组的数据
f2=e["arr_1"]  #提取第二个数组的数据

