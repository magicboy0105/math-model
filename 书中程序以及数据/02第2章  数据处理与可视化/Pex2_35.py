#程序文件Pex2_35.py
import pandas as pd
import numpy as np
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4)) #提取第1列到第4列的数据
b1=a.iloc[np.arange(6),[0,1]]  #通过标号筛选数据
b2=a.loc[np.arange(6),["用户A","用户B"]]  #通过标签筛选数据
