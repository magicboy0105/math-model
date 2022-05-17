#程序文件Pex2_19.py
import numpy as np
a=np.loadtxt("Pdata2_19.txt")  #返回值a为浮点型数据
b=a[0:2,1:4]  #获取a矩阵的第1,2行，第2,3,4列
print("b=",b)
