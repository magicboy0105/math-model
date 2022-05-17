#程序文件Pex2_30.py
import pandas as pd
import numpy as np
s=pd.Series([10.5,20.5,98],
            index=['a','b','c'])
a=s['b']  #取出序列的第2个元素，输出：20.5
b1=np.mean(s)  #输出：43.0
b2=s.mean()  #通过数列方法求均值，输出：43.0
