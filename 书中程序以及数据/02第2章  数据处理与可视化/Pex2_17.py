#程序文件Pex2_17.py
import numpy as np
a=np.arange(0, 20, 10).reshape(-1, 1)  #变形为1列的数组，行数自动计算
b=np.arange(0, 3)
print(a+b)
