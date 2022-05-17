#程序文件Pex2_14.py
import numpy as np
a=np.arange(10,15); b=np.arange(5,10)
c=a+b; d=a*b  #对应元素相加和相乘
e1=np.modf(a/b)[0]  #对应元素相除的小数部分
e2=np.modf(a/b)[1]  #对应元素相除的整数部分
