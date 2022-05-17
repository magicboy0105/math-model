#程序文件Pex2_33.py
import pandas as pd
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))  #提取第1列到第4列的数据
b=a.values  #提取其中的数据
c=a.describe()  #对数据进行统计描述
print(c)
