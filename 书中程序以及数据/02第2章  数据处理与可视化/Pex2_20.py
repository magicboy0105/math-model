#程序文件Pex2_20.py
import numpy as np
a=np.loadtxt("Pdata2_20.txt",dtype=str,delimiter="，")
b=a[1:,1:].astype(float)  #提取a矩阵的数值行和数值列，并转换类型
print("b=",b)
