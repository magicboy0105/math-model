#程序文件Pex2_13.py
import numpy as np
a=np.arange(4).reshape(2,2)  #构造2行2列的矩阵
b=np.hsplit(a,2)  #把a平均分成2个列数组
c=np.vsplit(a,2)  #把a平均分成2个行数组
print(b[0],'\n',b[1],'\n',c[0],'\n',c[1])
