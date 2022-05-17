#程序文件Pex2_29.py
import pandas as pd
import numpy as np
s1=pd.Series(np.array([10.5,20.5,30.5]))  #由数组构造序列
s2=pd.Series({"北京":10.5,"上海":20.5,"广东":30.5})  #由字典构造序列
s3= pd.Series([10.5,20.5,30.5],index=['b','c','d'])   #给出行标签命名
print(s1); print("--------------"); print(s2)
print("--------------"); print(s3)
